import json
import requests
import slack_presence
import unittest


class FunctionalTest(unittest.TestCase):

    @staticmethod
    def get_slack_presence():
        url = "https://slack.com/api/users.getPresence"
        url += f"?token={slack_presence.API_TOKEN}"
        response = requests.request("GET", url)
        if not response.ok:
            print(response.text)
            response.raise_for_status()
        presence = json.loads(response.text)['presence']
        if presence == 'active':
            presence = 'auto'
        return presence

    def setUp(self):
        self.presence = self.get_slack_presence()

    def tearDown(self):
        slack_presence.set_slack_presence(self.presence)

    def test_set_slack_presence_works(self):
        if self.presence == 'auto':
            slack_presence.set_slack_presence('away')
            self.assertEqual(self.get_slack_presence(), 'away')
        elif self.presence == 'away':
            slack_presence.set_slack_presence('auto')
            self.assertEqual(self.get_slack_presence(), 'auto')
