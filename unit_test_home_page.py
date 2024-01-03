import unittest
from unittest.mock import Mock
import tkinter as tk
from home_page import HomePage

class TestUpdateStatusMethod(unittest.TestCase):

    def setUp(self):
        # Setup a mock for root
        self.root_mock = tk.Tk()
        # Setup a mock for switch_frame
        self.switch_frame_mock = Mock()
        self.main_instance = HomePage(self.root_mock, self.switch_frame_mock)

    def test_update_status_connected(self):
        # Test the success case when status is 'connected'

        # Execute
        self.main_instance.update_status('connected')
        
        # Assert
        expected_text = 'Status: Medibot 1 connected'
        actual_text = self.main_instance.status_indicator.cget("text")
        self.assertEqual(actual_text, expected_text)

    def test_update_status_invalid_string(self):
        # Test the case when an invalid string is provided

        # Execute
        self.main_instance.update_status('invalid_status')
        
        # Assert
        expected_text = 'Status: disconnected'
        actual_text = self.main_instance.status_indicator.cget("text")
        self.assertEqual(actual_text, expected_text)

    def tearDown(self):
        # Clean up the Tkinter root after each test
        self.root_mock.destroy()

if __name__ == '__main__':
    unittest.main()
