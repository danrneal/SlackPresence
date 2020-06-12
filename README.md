# Slack Presence

This is a script meant to automatically manage your presence in Slack using Slack's API. The purpose of this script is to automatically manage changing your presence in Slack to "offline" during non-working hours. This allows you to read messages without showing you "online" where you may feel obligated to respond to a message that realistically can be left until morning. This also manages returning your presence to "online" during working hours so that coworkers know that you are online and available.

## Set-up

Set-up a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

You should see (env) before your command prompt now. (You can type `deactivate` to exit the virtual environment any time.)

Install the requirements:

```bash
pip install -U pip
pip install -r requirements.txt
```

Obtain a Slack API key [here](https://api.slack.com/apps).

- Configure the key in the "Permissions" option
- Under "Scopes -> User Token Scopes" include `users:write`
- Install your app to the desired workspace
- Copy the "OAuth Access Token" in the "Permissions option (it should start with "xoxp-")

Set the global variables `START_TIME` and `QUITTING_TIME` in `slack_presence.py`.

Set up your environment variables:

```bash
touch .env
echo SLACK_API_TOKEN="XXX" >> .env
```

## Usage

Make sure you are in the virtual environment (you should see (env) before your command prompt). If not `source /env/bin/activate` to enter it.

Make sure .env variables are set:

```bash
set -a; source .env; set +a
```

Then run the script:

```bash
Usage: slack_presence.py
```

## Deployment

For provisioning a new server see `deploy_tools/provisioning_notes.md`.

Set the host of your new server as an environment variable:

```bash
export HOST="YOU@HOST.COM"
```

You can deploy automatically to your new server using the following command:

```bash
fab deploy:host=$HOST
```

## Testing Suite

This repository contains a test suite consisting of functional tests and unit tests.

### Functional Tests

These test the program from the outside, from a user's point of view and are also known as Acceptance Tests or End-to-End Tests. You can run them with the following command:

```bash
python3 -m unittest discover functional_tests
```

#### _Note: These tests require that the Slack API Token also have the scope `users:read`_

### Unit Tests

These test the program from the inside, from the developer's point of view. You can run them with the following command:

```bash
python3 -m unittest discover tests
```

### A comment on TDD

This project was done following Test-Driven Development principles where the starting point is a failing test. My process was to write a unit test to define how I wanted the code to behave. That is the point where I wrote the "actual" code to get the unit tests to pass.

While this may seem unnecessary for a program of such a small size and may seem like overdoing, TDD principles help to create quality, maintainable code and as such I believe are good habits to foster even on a small project such as this.

## License

Slack Presence is licensed under the [MIT license](https://github.com/danrneal/slack-presence/blob/master/LICENSE).
