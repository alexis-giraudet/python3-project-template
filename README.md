# Python 3 Project Template

## Overview

```
.
├── debian
│   ├── changelog
│   ├── control
│   ├── copyright
│   ├── python3-project-template.install
│   ├── rules
│   └── source
│       └── format
├── LICENSE
├── mkosi.build
├── mkosi.builddir
├── mkosi.conf
├── mkosi.conf.d
│   └── ubuntu.conf
├── mkosi.prepare
├── pyproject.toml
├── README.md
├── src
│   └── mynamespace
│       └── myproject
│           ├── cli.py
│           ├── __init__.py
│           └── tui.py
├── tests
│   └── test_mytest.py
└── usr
    └── share
        └── applications
            └── myapplication-tui.desktop

12 directories, 18 files
```

## Getting started

[Creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

## Setup

[Creation of virtual environments](https://docs.python.org/3/library/venv.html)

### Debian/Ubuntu

Install system dependencies, create/activate a Python virtual environment and install Python dependencies:
```sh
sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip build whl2pyz pytest
```

## Develop

 - [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
 - [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

Install the application and make it editable (you don't have to reinstall it each time you edit the code):
```sh
python3 -m pip install --editable .
```

## Test

Run the tests:
```sh
pytest
```

## Build

Build source and wheel packages (output to ./dist/ folder):
```sh
python3 -m build
```

Build portable zip app (output to ./bin/ folder):
```sh
whl2pyz --python "/usr/bin/env python3" --compress -- .
```

# Debian package

## Build using mkosi

Build Debian package (output to ./mkosi.builddir/ folder):
```sh
mkosi build
# Build debug:
mkosi build -- -d
```

# References
 - [Python Packaging User Guide](https://packaging.python.org/en/latest/#)
 - [setuptools](https://setuptools.pypa.io/en/latest/#)
 - [A Comprehensive Guide to Python Project Management and Packaging: Concepts Illustrated with uv – Part I](https://reinforcedknowledge.com/a-comprehensive-guide-to-python-project-management-and-packaging-concepts-illustrated-with-uv-part-i/)
 - [pytest](https://docs.pytest.org/en/stable/#)
 - [PEP Index](https://peps.python.org/#)
 - [Black](https://black.readthedocs.io/en/stable/)
 - [zipapp - Manage executable Python zip archives](https://docs.python.org/fr/3/library/zipapp.html)
 - [mkosi — Build Bespoke OS Images](https://github.com/systemd/mkosi)
