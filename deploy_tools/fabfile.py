from fabric.contrib.files import exists
from fabric.api import cd, env, local, run

REPO_URL = 'git@gitlab.com:dan.r.neal/slack-presence.git'


def deploy():
    site_folder = f'/home/{env.user}/slack-presence'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('env/bin/pip'):
        run(f'python3 -m venv env')
    run('./env/bin/pip install -r requirements.txt')
