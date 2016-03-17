from setuptools import setup
 # -*- coding: utf-8 -*-

setup(
    name = 'watcher',
    version = '0.1.0',
    description = 'Execute command on file or folder change',
    author = 'Gérald Lelong',
    author_email = 'lelong.gerald@gmail.com',
    url = 'https://github.com/lelongg/watcher',
    scripts = [
        'watcher',
    ],
    install_requires = [
        'watchdog',
        'argparse',
    ],
)
