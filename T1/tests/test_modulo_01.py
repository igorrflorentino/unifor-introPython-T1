import unittest
from T1 import get_gdrive_file_ID

class TestGetGDriveFileID(unittest.TestCase):

    def test_valid_link_with_d(self):
        link = "https://drive.google.com/file/d/1A2B3C4D5E6F7G8H9/view?usp=sharing"
        expected = "1A2B3C4D5E6F7G8H9"
        self.assertEqual(get_gdrive_file_ID(link), expected)

    def test_valid_link_with_id(self):
        link = "https://drive.google.com/open?id=1A2B3C4D5E6F7G8H9"
        expected = "1A2B3C4D5E6F7G8H9"
        self.assertEqual(get_gdrive_file_ID(link), expected)

    def test_invalid_link(self):
        link = "https://example.com/file/invalid"
        expected = ""
        self.assertEqual(get_gdrive_file_ID(link), expected)

    def test_empty_link(self):
        link = ""
        expected = ""
        self.assertEqual(get_gdrive_file_ID(link), expected)

    def test_link_with_no_id(self):
        link = "https://drive.google.com/file/d/"
        expected = ""
        self.assertEqual(get_gdrive_file_ID(link), expected)

if __name__ == '__main__':
    unittest.main()
