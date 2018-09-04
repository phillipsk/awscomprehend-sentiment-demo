from unittest import TestCase
from unittest.mock import MagicMock
from comprehendApi import ComprehendApi


class TestComprehendapi(TestCase):
    def test_get_sentiment_singledoc(self):
        # Arrange
        data = "This is bad"
        mock_client = MagicMock()
        expected_sentiment = "negative"
        mock_client.detect_sentiment.return_value = {'Sentiment': 'NEGATIVE',
                                                     'SentimentScore': {
                                                         'Positive': 0,
                                                         'Negative': 1.0,
                                                         'Neutral': 0,
                                                         'Mixed': 0
                                                     }}
        sut = ComprehendApi(mock_client)

        # Act

        actual_sentiment, confidence_score = sut.get_sentiment_singledoc(data, 'en')

        # Assert
        self.assertEqual(actual_sentiment.lower(), expected_sentiment)
        self.assertEqual(confidence_score, 1.0)

    def test_get_sentiment_batch_bulk(self):
        # Arrange
        data = ["This is bad"
            , "This is good"]
        mock_client = MagicMock()

        # Response looks like this for batch sentiment

        mock_client.batch_detect_sentiment.return_value =  {
            'ResultList': [
                {
                    'Index': 1,
                    'Sentiment': 'POSITIVE' ,
                    'SentimentScore': {
                        'Positive': 1.0,
                        'Negative': 0.0,
                        'Neutral': 0.0,
                        'Mixed': 0.0
                    }
                },
                {
                    'Index': 0,
                    'Sentiment': 'NEGATIVE',
                    'SentimentScore': {
                        'Positive': 0.1,
                        'Negative': .8,
                        'Neutral': 0.1,
                        'Mixed': 0.0
                    }
                },
            ],
            'ErrorList': [

            ]
        }


        sut = ComprehendApi(mock_client)

        # Act
        actual = sut.get_sentiment_batch_bulk(data)

        # Assert
        self.assertEqual(len(data), len(actual))
