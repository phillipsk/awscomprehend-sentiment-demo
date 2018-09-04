from unittest import TestCase

from source.comprehendApi import ComprehendApi


class TestComprehendapi(TestCase):
    def test_single(self):
        # Arrange
        sut = ComprehendApi()

        # Act
        actual_sentiment, confidence_score = sut.get_sentiment_singledoc("This is bad")
        expected_sentiment = "negative"

        # Assert
        self.assertEqual(actual_sentiment.lower(), expected_sentiment)
        self.assertGreater(confidence_score, 0)
