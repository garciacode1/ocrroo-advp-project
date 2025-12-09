from pathlib import Path
import unittest
from backend.preliminary.library_basics import path_checker, BASE_PATH

@path_checker
def fake_loader(video_path):
    """Test helper that only retuns video path after it is passed thru decorator"""
    return video_path

class TestPathChecker(unittest.TestCase):
    """"Test for path checker decorator that checks if paths are vaidated and converted accurately"""

    def test_relative_path_becomes_absolute(self):
        """this unittest checks if relative path is correctly converted to absolute path
            the decorator should check if its a relative path, added to BASE_PATH,
            and tehn, resolve it into a full absolute file ppath"""
        relative = "resources/oop.mp4"

        result = fake_loader(relative)
        expected = (BASE_PATH / relative).resolve()

        self.assertEqual(str(result), str(expected))



if __name__ == "__main__":
    unittest.main()

