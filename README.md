# Slack Presence

This is a script meant to automatically manage your presence in Slack using Slack's API. The purpose of this script is to automatically manage changing your presence in Slack to "offline" during non-working hours. This allows you to read messages without showing you "online" where you may feel obligated to respond to a message that realistically can be left until morning. This also manages returning your presence to "online" during working hours so that coworkers know that you are online and available.

## Set-up

Set-up a virtual environment and activate it:

```shell
python3 -m venv venv
source venv/bin/activate
```

You should see (venv) before your command prompt now. (You can type `deactivate` to exit the virtual environment any time.)

Install the requirements:

```shell
pip install -r requirements.txt
```

Set up your environment variables:

```shell
touch .env
echo SLACK_API_TOKEN="XXX" >> .env
```

## Usage

Make sure you are in the virtual environment (you should see (venv) before your command prompt). If not `source /venv/bin/activate` to enter it.

Make sure .env variables are set:

```shell
set -a; source .env; set +a
```

Then set the global variables START_TIME and QUITTING_TIME in slack_presence.py

```shell
Usage: scraper.py
```

## Testing Suite

This repository contains a test suite consisting of unit tests.

### Unit Tests

These test the program from the inside, from the developer's point of view. You can run them with the following command:

```shell
python3 -m unittest discover tests/
```

## A comment on TDD

This project was done following Test-Driven Development principles where the starting point is a failing test. My process was to write a unit test to define how I wanted the code to behave. That is the point where I wrote the "actual" code to get the unit tests to pass.

While this may seem unnecessary for a program of such a small size and may seem like overdoing, TDD principles help to create quality, maintainable code and as such I believe are good habits to foster even on a small project such as this.

## License

Udacity Link Scraper is licensed under the [MIT license](https://github.com/danrneal/slack-presence/blob/master/LICENSE).
