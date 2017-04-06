import requests


def vscode():
    response = requests.get('https://github.com/atom/atom/releases/lastest')
    latest_version = response.url.split('/')[-1]

    return [
        ('MacOS', 'https://vscode-update.azurewebsites.net/latest/darwin/stable', 'vscode/vscode-{}-macos.zip'.format(latest_version)),  # noqa
        ('Windows', 'https://vscode-update.azurewebsites.net/latest/win32/stable', 'vscode/vscode-{}-windows.exe'.format(latest_version)),  # noqa
        ('Ubuntu', 'https://vscode-update.azurewebsites.net/latest/linux-deb-x64/stable', 'vscode/vscode-{}-ubuntu.deb'.format(latest_version)),  # noqa
    ]
