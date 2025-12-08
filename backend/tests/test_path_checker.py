import sys
from pathlib import Path
import unittest
from backend.preliminary.library_basics import path_checker, BASE_PATH

@path_checker
def fake_loader(video_path):
    return video_path

class TestPathChecker(unittest.TestCase):

    def test_relative_path_becomes_absolute(self):
        relative = "resources/oop.mp4"

        result = fake_loader(relative)
        expected = (BASE_PATH / relative).resolve()

        self.assertEqual(str(result), str(expected))


if __name__ == "__main__":
    unittest.main()

