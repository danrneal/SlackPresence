import os
import requests
import schedule
import time

API_TOKEN = os.environ['SLACK_API_TOKEN']
START_TIME = '10:00'
QUITTING_TIME = '18:00'


def set_slack_presence(presence):
    url = "https://slack.com/api/users.setPresence"
    url += f"?token={API_TOKEN}"
    url += f"&presence={presence}"
    response = requests.request("POST", url)
    if not response.ok:
        print(response.text)
        response.raise_for_status()


schedule.every().monday.at(START_TIME).do(
    set_slack_presence,
    presence='auto'
)
schedule.every().monday.at(QUITTING_TIME).do(
    set_slack_presence,
    presence='away'
)
schedule.every().tuesday.at(START_TIME).do(
    set_slack_presence,
    presence='auto'
)
schedule.every().tuesday.at(QUITTING_TIME).do(
    set_slack_presence,
    presence='away'
)
schedule.every().wednesday.at(START_TIME).do(
    set_slack_presence,
    presence='auto'
)
schedule.every().wednesday.at(QUITTING_TIME).do(
    set_slack_presence,
    presence='away'
)
schedule.every().thursday.at(START_TIME).do(
    set_slack_presence,
    presence='auto'
)
schedule.every().thursday.at(QUITTING_TIME).do(
    set_slack_presence,
    presence='away'
)
schedule.every().friday.at(START_TIME).do(
    set_slack_presence,
    presence='auto'
)
schedule.every().friday.at(QUITTING_TIME).do(
    set_slack_presence,
    presence='away'
)
while True:
    schedule.run_pending()
    time.sleep(1)
