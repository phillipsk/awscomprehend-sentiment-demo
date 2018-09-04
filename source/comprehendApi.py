import boto3




class ComprehendApi:

    def get_sentiment_singledoc(self, text: str, language_code: str = 'es') -> str:
        client = boto3.client('comprehend')

        result = client.detect_sentiment(Text=text, LanguageCode=language_code)

        sentiment = result["Sentiment"]
        confidence_score = result["SentimentScore"][sentiment.title()]


        return sentiment, confidence_score
