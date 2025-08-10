import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def _assert_dominant(self, text, expected):
        result = emotion_detector(text)
        self.assertIsInstance(result, dict)
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], expected)

    def test_joy(self):
        self._assert_dominant("I am glad this happened", "joy")
    
    def test_anger(self):
        self._assert_dominant("I am really mad about this", "anger")

    def test_disgust(self):
        self._assert_dominant("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self._assert_dominant("I am so sad about this", "sadness")

    def test_fear(self):
        self._assert_dominant("I am really afraid that this will happen", "fear")

if __name__ == "__main__":
    unittest.main()