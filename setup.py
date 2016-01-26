#!/usr/bin/env python

import os
import re
import sys

from setuptools import setup

with open('cagezzz/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError('Cannot find version')

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
]

setup(
    name = 'cagezzz',
    packages = ['cagezzz'],
    version = version,
    description = 'A package for getting more Cage in your life',
    author = 'Richard Hydomako',
    author_email = 'rhydomako@gmail.com',
    url = 'https://github.com/rhydomako/cagezzz',
    classifiers = classifiers,
    long_description = readme,
    license = license,
    package_data = {
        "cagezzz": [
            "cagezzz.txt",
            "../LICENSE",
            "../README.md",
        ]
    }
)
