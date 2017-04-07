#!/usr/bin/env python3

import os
from subprocess import run, Popen

from jinja2 import Environment, PackageLoader

from finders.atom import atom
from finders.py35 import py35
from finders.git import git
from finders.vscode import vscode
from finders.bootstrap import bootstrap
from finders.sublime import sublime
from finders.gedit import gedit


DOWNLOAD_BASE = 'www'
ORGANISATION_NAME = 'Common Code'
SLACK_URL = 'https://melbdjango-slackin.herokuapp.com/'


DJANGOGIRLS_RESOURCES = [{
    'name': 'Frameworks and Tools',
    'finders': [
        ('Python 3.5', py35),
        ('Git', git),
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


def django_docs():
    outdir = os.path.join(DOWNLOAD_BASE, 'docs/django-1.10')

    path = download_url('https://docs.djangoproject.com/m/docs/django-docs-1.10-en.zip', 'docs/django-docs-1.10-en.zip')
    os.makedirs(outdir, exist_ok=True)
    run(['unzip', '-o', path, '-d', outdir])

    return {
        'name': 'Django 1.10',
        'downloads': [{
                'name': 'View Online',
                'url': outdir.replace(DOWNLOAD_BASE, ''),
            }, {
                'name': 'Download',
                'url': path.replace(DOWNLOAD_BASE, ''),
            }
        ]
    }


def djangogirls():
    run(['git', 'clone', 'https://github.com/DjangoGirls/tutorial.git'])
    
    install = Popen(['../node_modules/.bin/gitbook', 'install'], cwd='tutorial')
    install.wait()

    build = Popen(['../node_modules/.bin/gitbook', 'build', '.'], cwd='tutorial')
    build.wait()

    run(['mv', 'tutorial/_book', os.path.join(DOWNLOAD_BASE, 'docs', 'djangogirls')])
    return {
        'name': 'Django Girls Tutorial',
        'downloads': [{
            'name': 'View Online',
            'url': 'docs/djangogirls/en/',
        }]
    }


def python35():
    download_url(
        'https://docs.python.org/3.5/archives/python-3.5.3-docs-html.tar.bz2',
        os.path.join('python', 'python-3.5.3-docs-html.tar.bz2')
    )

    outdir = os.path.join(DOWNLOAD_BASE, 'docs/python-35')
    os.makedirs(outdir, exist_ok=True)
    run(['tar', '-xf', os.path.join(DOWNLOAD_BASE, 'python', 'python-3.5.3-docs-html.tar.bz2'), '-C', outdir])

    return {
        'name': 'Python 3.5',
        'downloads': [{
            'name': 'View Online',
            'url': 'docs/python-35/python-3.5.3-docs-html/'
        }, {
            'name': 'Download',
            'url': os.path.join('python', 'python-3.5.3-docs-html.tar.bz2'),
        }]
    }


def main():
    resources = []

    # do the documentation manually
    documentation = {'name': 'Documentation', 'section_items': []}
    documentation['section_items'].extend([
        djangogirls(),
        django_docs(),
        python35(),
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
