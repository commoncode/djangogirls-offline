import requests


def bootstrap():
    response = requests.get('https://github.com/twbs/bootstrap/releases/latest')
    latest_version = response.url.split('/')[-1]

    return [
        ('Download', 'https://github.com/twbs/bootstrap/releases/download/{}/bootstrap-{}-dist.zip'.format(
            latest_version, latest_version.replace('v', '')
        ), 'bootstrap/bootstrap-{}-dist.zip'.format(latest_version))
    ]
