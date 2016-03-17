spekti
======

Summary
-------

Execute command on file or folder event.

Caution
-------

**This software is still in experimental stages.** Please report any bug you might encounter.

Description
-----------

Watch a file or a folder and execute provided command on any modification.

Synopsis
--------

  usage: spekti [-h] path command
  
  Execute command on file or folder event
  
  positional arguments:
    path        watched file or folder
    command     command to execute
  
  optional arguments:
    -h, --help  show this help message and exit

Prerequisites
-------------

- python

Dependencies (automatically installed)
--------------------------------------

- watchdog `pip install watchdog`
- argparse `pip install argparse`

Installation
------------

### From PyPI

`pip install spekti`

OR

### From sources

  git clone https://github.com/lelongg/spekti.git
  cd spekti
  python setup.py install

Quick start
-----------

  spekti . "echo This folder has been modified"
  
The message "This folder has been modified" will be displayed every time you add, remove or modify files in the current folder.
