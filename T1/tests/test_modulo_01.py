# Import the unittest module for unit testing.
import unittest
# Import the function to be tested.
from T1 import get_gdrive_file_ID

# Define a test class for the `get_gdrive_file_ID` function.
class TestGetGDriveFileID(unittest.TestCase):

    # Test a valid link with the standard "/d/" format.
    def test_valid_link_with_d(self):
        link = "https://drive.google.com/file/d/1A2B3C4D5E6F7G8H9/view?usp=sharing"
        expected = "1A2B3C4D5E6F7G8H9"
        # Check if the function correctly extracts the ID.
        self.assertEqual(get_gdrive_file_ID(link), expected, f"Failed to extract ID from link: {link}")

    # Test a valid link using the alternative "id=" format.
    def test_valid_link_with_id(self):
        link = "https://drive.google.com/open?id=1A2B3C4D5E6F7G8H9"
        expected = "1A2B3C4D5E6F7G8H9"
        # Check if the function correctly extracts the ID in this format.
        self.assertEqual(get_gdrive_file_ID(link), expected, f"Failed to extract ID from link: {link}")

    # Test an invalid link that does not belong to Google Drive.
    def test_invalid_link(self):
        link = "https://example.com/file/invalid"
        expected = ""
        # An invalid link is expected to return an empty string.
        self.assertEqual(get_gdrive_file_ID(link), expected, f"Failed to handle invalid link: {link}")

    # Test the case of an empty input.
    def test_empty_link(self):
        link = ""
        expected = ""
        # Ensure the function handles an empty input properly.
        self.assertEqual(get_gdrive_file_ID(link), expected, "Failed to handle empty link")

    # Test a Google Drive link with no valid ID.
    def test_link_with_no_id(self):
        link = "https://drive.google.com/file/d/"
        expected = ""
        # Check if the function returns an empty string for incomplete links.
        self.assertEqual(get_gdrive_file_ID(link), expected, f"Failed to handle link with no ID: {link}")

    # Test a malformed link with no valid Google Drive structure.
    def test_malformed_link(self):
        link = "drive.google.com/file/1A2B3C4D5E6F7G8H9"
        expected = ""
        # Check if the function returns an empty string for a malformed link.
        self.assertEqual(get_gdrive_file_ID(link), expected, f"Failed to handle malformed link: {link}")

# Check if the file is executed directly, and if so, run the tests.
if __name__ == '__main__':
    unittest.main()
