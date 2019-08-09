Provisioning a new site
=======================

## Required packages:

* Python 3
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo apt update
    sudo apt install git python3 python3-venv

## Systemd service

* see gunicorn-systemd.template.service
* replace USER with, e.g., user

## Folder structure:

Assume we have a user account at /home/username

/home/username

    └── slack-presence
        ├── .env
        ├── env
        ├── functional_tests
        ├── slack_presence.py
        └── tests