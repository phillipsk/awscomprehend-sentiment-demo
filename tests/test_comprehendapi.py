from unittest import TestCase

from comprehendApi import ComprehendApi


class TestComprehendapi(TestCase):
    def test_get_sentiment_singledoc(self):
        # Arrange
        sut = ComprehendApi()

        # Act
        actual_sentiment, confidence_score = sut.get_sentiment_singledoc("This is bad")
        expected_sentiment = "negative"

        # Assert
        self.assertEqual(actual_sentiment.lower(), expected_sentiment)
        self.assertGreater(confidence_score, 0)

    def test_get_sentiment_batch(self):
        # Arrange
        sut = ComprehendApi()
        data = ["This is bad"
            , "This is good"]

        # Act
        actual = sut.get_sentiment_batch(data)

        # Assert
        self.assertEqual(len(data), len(actual))

