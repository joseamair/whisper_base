import unittest
import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from whisper_utils import whisper_tools

class TestTranscribeFunction(unittest.TestCase):

    def test_transcribe_valid_file(self):
        # Test when providing a valid audio file
        filepath = "../test_audios/input_audios/audio_1.mp3"
        success, result = whisper_tools.transcribe(filepath)

        self.assertTrue(success)
        self.assertIn("transcript", result)
        self.assertIn("no_speech_prob", result)
        self.assertIn("language", result)

        # Add more specific assertions based on the expected output of the function
        # For example, you might want to check if the transcript, no_speech_prob, and language are of the correct data types or within certain ranges.

    def test_transcribe_invalid_file(self):
        # Test when providing an invalid file path
        filepath = "../test_audios/input_audios/audio_0.mp3"
        success, result = whisper_tools.transcribe(filepath)

        self.assertFalse(success)
        self.assertEqual(result, {})

    def test_transcribe_only_transcription(self):
        # Test when get_language=False and transcribe=True
        filepath = "../test_audios/input_audios/audio_1.mp3"
        success, result = whisper_tools.transcribe(filepath, get_language=False, transcribe=True)

        self.assertTrue(success)
        self.assertIn("transcript", result)
        self.assertNotIn("language", result)
        self.assertNotIn("no_speech_prob", result)

    def test_transcribe_with_language_detection(self):
        # Test when get_language=True and transcribe=True
        filepath = "../test_audios/input_audios/audio_1.mp3"
        success, result = whisper_tools.transcribe(filepath, get_language=True, transcribe=True)

        self.assertTrue(success)
        self.assertIn("transcript", result)
        self.assertIn("language", result)
        self.assertIn("no_speech_prob", result)

    # Add more tests for different scenarios, edge cases, and any custom behavior you want to validate.

if __name__ == "__main__":
    unittest.main()
