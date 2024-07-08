import unittest
from unittest.mock import patch

from unbabel_app.tasks.dataload import load_data

class TestDataload(unittest.TestCase):
    @patch("pandas.read_json")
    def test_load_data(self, mock_read_json):
        file_input = "test_input.json"
        load_data(file_input)

        mock_read_json.assert_called_once_with(file_input, lines=True)
        
    