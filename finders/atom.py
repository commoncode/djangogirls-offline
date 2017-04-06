import requests


def atom():
    response = requests.get('https://github.com/atom/atom/releases/latest')
    latest_version = response.url.split('/')[-1]

    return [
        ('MacOS', 'https://github.com/atom/atom/releases/download/{}/atom-mac.zip'.format(latest_version), 'atom/atom-mac.zip'),
        ('Windows', 'https://github.com/atom/atom/releases/download/{}/atom-x64-windows.zip'.format(latest_version), 'atom/atom-x64-windows.zip'),  # noqa
        ('Ubuntu', 'https://github.com/atom/atom/releases/download/{}/atom-amd64.deb'.format(latest_version), 'atom/atom-amd64.deb')
    ]
