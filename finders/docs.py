import os

from subprocess import Popen, run
from djangogirls import download_url, DOWNLOAD_BASE


def django():
    outdir = os.path.join(DOWNLOAD_BASE, 'docs/django-1.10')

    path = download_url('https://docs.djangoproject.com/m/docs/django-docs-1.10-en.zip', 'docs/django-docs-1.10-en.zip')
    os.makedirs(outdir, exist_ok=True)
    run(['unzip', '-o', path, '-d', outdir])

    return {
        'name': 'Django 1.10',
        'downloads': [{
                'name': 'View Online',
                'url': 'docs/django-1.10',
            }, {
                'name': 'Download',
                'url': 'docs/django-docs-1.10-en.zip',
            }
        ]
    }


def djangogirls(skip_build=False):
    if not skip_build:
        run(['git', 'clone', 'https://github.com/DjangoGirls/tutorial.git'])

        pull = Popen(['git', 'pull'], cwd='tutorial')
        pull.wait()

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
