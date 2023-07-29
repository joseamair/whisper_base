import subprocess
import unittest

def is_ffmpeg_installed():
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)

        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

class TestFFmpegInstallation(unittest.TestCase):
    def test_ffmpeg_installed(self):
        self.assertTrue(is_ffmpeg_installed(), "ffmpeg is installed on the system.")

if __name__ == '__main__':
    unittest.main()
