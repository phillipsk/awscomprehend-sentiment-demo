import argparse

import boto3


class ComprehendApi:

    def get_sentiment_singledoc(self, text: str, language_code: str = 'es') -> tuple:
        client = boto3.client('comprehend')
        response = client.detect_sentiment(Text=text, LanguageCode=language_code)

        sentiment = response["Sentiment"]
        confidence_score = response["SentimentScore"][sentiment.title()]

        return sentiment, confidence_score

    def get_sentiment_batch(self, list_of_doc: list, language_code: str = 'es') -> list:
        client = boto3.client('comprehend')

        # Response looks like this for batch sentiment
        # {
        #     'ResultList': [
        #         {
        #             'Index': 123,
        #             'Sentiment': 'POSITIVE' | 'NEGATIVE' | 'NEUTRAL' | 'MIXED',
        #             'SentimentScore': {
        #                 'Positive': ...,
        #                 'Negative': ...,
        #                 'Neutral': ...,
        #                 'Mixed': ...
        #             }
        #         },
        #     ],
        #     'ErrorList': [
        #         {
        #             'Index': 123,
        #             'ErrorCode': 'string',
        #             'ErrorMessage': 'string'
        #         },
        #     ]
        # }
        response = client.batch_detect_sentiment(TextList=list_of_doc, LanguageCode=language_code)

        # Error handling
        error_list = response['ErrorList']
        if len(error_list) > 0:
            error_msg = '\n'.join(['{} {}'.format(e['Index'], e['ErrorMessgae']) for e in error_list])
            raise RuntimeError(error_msg)

        result = []
        for r in response['ResultList']:
            input_index = r['Index']
            text = list_of_doc[input_index]
            sentiment = r["Sentiment"]
            confidence_score = r["SentimentScore"][sentiment.title()]

            result.append((text, sentiment, confidence_score))

        return result


