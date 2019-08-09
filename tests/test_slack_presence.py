import unittest
from unittest.mock import Mock, patch
import slack_presence


class SlackPresenceTest(unittest.TestCase):

    @patch('requests.request')
    def test_set_slack_presence(self, mock_request):
        mock_request.return_value = Mock()
        mock_request.return_value.status_code = 200
        mock_request.return_value.text = 'ok'
        slack_presence.set_slack_presence('away')
        url = "https://slack.com/api/users.setPresence"
        url += f"?token={slack_presence.API_TOKEN}"
        url += f"&presence=away"
        mock_request.assert_called_once_with('POST', url)
