import unittest
from unittest.mock import patch
from login_page import LoginPage
from db import auth, sign_in

class TestLoginPageIntegration(unittest.TestCase):

    @patch('db.auth.get_user_by_email')
    def test_check_credentials_successful_login(self, mock_get_user_by_email):
        # Mock the get_user_by_email function to simulate a successful login
        mock_get_user_by_email.return_value = {'uid': 'user_id'}

        # Create an instance of LoginPage
        login_page = LoginPage(root=None, switch_frame=lambda x: None)

        # Set username and password
        login_page.username_text_field.insert(0, 'holdt@interim.hos')
        login_page.password_text_field.insert(0, 'qwert123')

        # Call the check_credentials method
        login_page.check_credentials(switch_frame=lambda x: self.assertEqual(x, "Home"))

        # Assert that the mock_get_user_by_email was called with the correct arguments
        mock_get_user_by_email.assert_called_once_with(email='holdt@interim.hos')

    @patch('db.auth.get_user_by_email')
    def test_check_credentials_failed_login(self, mock_get_user_by_email):
        # Mock the get_user_by_email function to simulate a failed login
        mock_get_user_by_email.side_effect = auth.AuthError("Error message")

        # Create an instance of LoginPage
        login_page = LoginPage(root=None, switch_frame=lambda x: None)

        # Set username and password
        login_page.username_text_field.insert(0, 'invalid_user@interim.hos')
        login_page.password_text_field.insert(0, 'invalid_password')

        login_page.check_credentials(switch_frame=lambda x: self.fail("Switch_frame should not be called"))

        # Assert that the mock_get_user_by_email was called with the correct arguments
        mock_get_user_by_email.assert_called_once_with(email='invalid_user@interim.hos')

if __name__ == '__main__':
    unittest.main()
