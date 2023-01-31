# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
else:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='apimatic-core',
    version='0.2.0',
    description='A library that contains core logic and utilities for '
                'consuming REST APIs using Python SDKs generated by APIMatic.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='APIMatic',
    author_email='support@apimatic.io',
    url='https://github.com/apimatic/core-lib-python',
    packages=find_packages(),
    install_requires=[
        'apimatic-core-interfaces~=0.1.0',
        'jsonpickle~=1.4, >= 1.4.1',
        'python-dateutil~=2.8.1',
        'requests~=2.28.1',
        'enum34~=1.1, >=1.1.10',
        'setuptools~=65.5.1',
        'jsonpointer~=2.3'
    ],
    tests_require=[
        'pytest~=7.1.3',
        'pytest-cov~=3.0.0'
    ]
)
