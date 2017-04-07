#!/usr/bin/env python3

import os
import sys
from subprocess import run, Popen

from jinja2 import Environment, PackageLoader

from finders.atom import atom
from finders.py35 import py35, cheatsheet
from finders.git import git
from finders.vscode import vscode
from finders.bootstrap import bootstrap
from finders.sublime import sublime
from finders.gedit import gedit
from finders import docs


DOWNLOAD_BASE = 'www'
ORGANISATION_NAME = 'Common Code'
SLACK_URL = 'https://melbdjango-slackin.herokuapp.com/'


DJANGOGIRLS_RESOURCES = [{
    'name': 'Frameworks and Tools',
    'finders': [
        ('Python 3.5', py35),
        ('Git', git),
        ('Python Cheatsheet', cheatsheet),
    ]
}, {
    'name': 'Editors',
    'finders': [
        ('Atom', atom),
        ('VS Code', vscode),
        ('Sublime Text 3', sublime),
        ('Gedit', gedit)
    ]
}, {
    'name': 'CSS Frameworks and Fonts',
    'finders': [
        ('Bootstrap', bootstrap),
    ]
}]


def download_url(url, target_path):
    target_path = os.path.join(DOWNLOAD_BASE, target_path)

    if not os.path.exists(target_path):
        cmd = ['curl', '--create-dirs', '-o', target_path, '-L', url]
        run(cmd)

    return target_path


def main():
    resources = []

    # do the documentation manually
    documentation = {'name': 'Documentation', 'section_items': []}
    documentation['section_items'].extend([
        docs.djangogirls(skip_build='--skip-tutorial' in sys.argv),
        docs.django(),
        docs.python35(),
    ])
    resources.append(documentation)

    for section in DJANGOGIRLS_RESOURCES:
        s = {}
        s['name'] = section['name']
        s['section_items'] = []
        for name, finder in section['finders']:
            item = {
                'name': name,
                'downloads': []
            }

            for platform, url, local_path in finder():
                download_url(url, local_path)
                item['downloads'].append({
                    'name': platform,
                    'url': local_path,
                })
            s['section_items'].append(item)

        resources.append(s)

    env = Environment(loader=PackageLoader('djangogirls', 'templates'))
    template = env.get_template('template.html')

    with open(os.path.join(DOWNLOAD_BASE, 'index.html'), 'w') as f:
        f.write(template.render(
            resources=resources,
            organisation=ORGANISATION_NAME,
            slack=SLACK_URL
        ))


if __name__ == '__main__':
    main()
