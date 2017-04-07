`djangogirls-offline` is a Python script that downloads the content needed to run a DjangoGirls workshop on a slow internet connection.
It aims to provide all large files that will be needed to run the workshop, as well as relevant documentation.

Currently targeting support for MacOS, Windows and Ubuntu.

There are still online components to the tutorial that will require internet access (including install Django itself!).


## Getting Started

Ensure that you have Python 3.5, curl, gitbook-cli, and git.

```
sudo apt-get install npm
sudo apt-get install nodejs-legacy
sudo npm install yarn

cd djangogirls-offline
yarn install
```

You should use a virtualenvironment with Jinja2 and requests.
From the `djangogirls-offline` directory:

```
python3 -m venv myvenv
source myvenv/bin/activate
pip install jinja2 requests
```


## What's Downloaded

Libraries / frameworks:

- [x] Python 3.5.x
- [x] Git
- [ ] PyPI Dev Server with:
    - [ ] pip + dependencies
    - [ ] Django 1.10.x
    - [ ] Pytz

Editors:

- [x] Atom
- [x] VS Code
- [x] Sublime Text (Commercial)
- [x] Gedit


CSS / Fonts

- [x] Bootstrap 3.x
- [ ] Lobster font

Documentation:

- [x] The Django Girls Tutorial
- [x] Django 1.10.x
- [x] Python 3.5.x
- [ ] Bootstrap 3.x
