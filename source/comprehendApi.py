from functools import reduce

import boto3
from multiprocessing.dummy import Pool as ThreadPool
from itertools import product


class ComprehendApi:

    def __init__(self, aws_service, client=None):
        self.client = client or boto3.client('comprehend')
        self.get_aws_service(aws_service)

    def get_aws_service(self, aws_service):
        if aws_service in 'batch_detect_dominant_language':
            self.aws_service = 'det_lang'
        if aws_service in 'batch_detect_entities':
            self.aws_service = 'det_entities'
        if aws_service in 'batch_detect_key_phrases':
            self.aws_service = 'det_phrases'
        if aws_service in 'batch_detect_sentiment':
            self.aws_service = 'det_sent'
        if aws_service in 'batch_detect_syntax':
            self.aws_service = 'det_syntax'

    def get_sentiment_singledoc(self, text: str, language_code: str = 'en') -> tuple:
        """
Obtains sentiment for a single text
        :param text: The text
        :param language_code: Langauge code
        :return: tuple (sentiment, confidencescore)
        """
        response = self.client.detect_sentiment(Text=text, LanguageCode=language_code)

        sentiment = response["Sentiment"]
        confidence_score = response["SentimentScore"][sentiment.title()]

        return sentiment, confidence_score

    def get_comprehend_batch_bulk(self, list_of_doc: list, language_code: str = 'en', max_threads=10) -> list:
        """
Obtains sentiment for a batch of documents. Comprehend api only accepts 25  documents at time, so this splits a list into chunks .
        :param list_of_doc: list of documents
        :param language_code: The language code
        :return: a list of sentiments
        """
        pool = ThreadPool(max_threads)
        result = pool.starmap(self.get_comprehend_batch,
                              product(self._chunks(list_of_doc, chunk_size=20), [language_code]))
        pool.close()
        pool.join()
        result = reduce(lambda x, y: x + y, result)
        return result

    def get_comprehend_batch(self, list_of_doc, language_code):
        # Comprehend api only accepts 25  documents at time
        assert len(list_of_doc) <= 25

        if self.aws_service in "det_sent":
            response = self.client.batch_detect_sentiment(TextList=list_of_doc, LanguageCode=language_code)
            # response = self.client.batch_detect_key_phrases(TextList=list_of_doc, LanguageCode=language_code)
            # Error handling
            error_list = response['ErrorList']
            if len(error_list) > 0:
                error_msg = '\n'.join(['{} {}'.format(e['Index'], e['ErrorMessage']) for e in error_list])
                raise RuntimeError(error_msg)
            # Collect results
            result = []
            for r in response['ResultList']:
                input_index = r['Index']
                text = list_of_doc[input_index]
                sentiment = r["Sentiment"]
                confidence_score = r["SentimentScore"][sentiment.title()]

                result.append((text, sentiment, confidence_score))
            return result
        elif self.aws_service in 'det_phrases':
            response = self.client.batch_detect_key_phrases(TextList=list_of_doc, LanguageCode=language_code)
            # Error handling
            error_list = response['ErrorList']
            if len(error_list) > 0:
                error_msg = '\n'.join(['{} {}'.format(e['Index'], e['ErrorMessage']) for e in error_list])
                raise RuntimeError(error_msg)
            # Collect results
            result = []
            for r in response['ResultList']:
                if len(r['KeyPhrases']) == 0:
                    continue
                else:
                    input_index = r['Index']
                    text = list_of_doc[input_index]
                    score = r['KeyPhrases'][0]['Score']
                    keyText = r['KeyPhrases'][0]['Text']

                    result.append((text, keyText, score))
            return result

    def _chunks(self, list, chunk_size=20):

        """Yield successive n-sized chunks from l."""
        for i in range(0, len(list), chunk_size):
            yield list[i:i + chunk_size]
