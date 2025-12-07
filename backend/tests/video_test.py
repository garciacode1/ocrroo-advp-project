import unittest
from pathlib import Path
from fastapi import HTTPException
from unittest.mock import patch
from preliminary.simple_api import _open_vid_or_404, VIDEOS


class TestVideoPlayback(unittest.TestCase):
    def test_404_if_file_does_not_exist(self):
        mock_path = Path("/this/is/my/fake/path.mp4")
        VIDEOS["missing_file"] = mock_path

        with patch.object(Path,"is_file", return_value=False):
            with self.assertRaises(HTTPException) as response:
                _open_vid_or_404("missing_file")

        self.assertEqual(response.exception.status_code,404)
        self.assertEqual(response.exception.detail,"Video not found")

    def test():
        coding_vid = CodingVideo("../resources/oop.mp4")
        print(coding_vid)

        # getting frame from video (no OCR)
        coding_vid.get_image_as_bytes(42)
        coding_vid.save_as_image(42)

        # getting frame, and 'OCRing' it
        print(coding_vid.get_text_from_frame_at_time(42))


#if __name__ == '__main__':
    #unittest.main()
if __name__ == '__main__':
    test()