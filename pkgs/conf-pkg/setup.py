#! /usr/bin/env python

'''Setup file for libs.conf

See:
    https://packaging.python.org/en/latest/distributing.html
'''

import os
import re

from setuptools import setup, find_packages

def read(*paths):
    '''read and return txt content of file'''
    with open(os.path.join(*paths)) as fp:
        return fp.read()


def find_version(*paths):
    '''reads a file and returns the defined __version__ value'''
    version_match = re.search(r"^__version__ ?= ?['\"]([^'\"]*)['\"]",
                              read(*paths), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

# compute version range
version = find_version('src', 'genie', 'libs', 'conf', '__init__.py')

install_requires = []

# launch setup
setup(
    name = 'genie.libs.conf',
    version = version,

    # descriptions
    description = 'Genie libs Conf: Libraries to configures topology through Python object attributes',
    long_description = read('DESCRIPTION.rst'),

    # the project's main homepage.
    url = 'https://developer.cisco.com/site/pyats/',

    # author details
    author = 'Cisco Systems Inc.',
    author_email = 'pyats-support-ext@cisco.com',

    # project licensing
    license = 'Apache 2.0',

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # project keywords
    keywords = 'genie pyats test automation',

    # uses namespace package
    namespace_packages = ['genie', 'genie.libs'],

    # project packages
    packages = find_packages(where = 'src'),

    # project directory
    package_dir = {
        '': 'src',
    },

    # additional package data files that goes into the package itself
    package_data = {
    },

    # console entry point
    entry_points = {
    },

    # package dependencies
    install_requires = install_requires,

    # any additional groups of dependencies.
    # install using: $ pip install -e .[dev]
    extras_require = {
        'dev': ['coverage',
                'restview',
                'Sphinx',
                'sphinxcontrib-napoleon',
                'sphinx-rtd-theme'],
    },

    # external modules
    ext_modules = [],

    # any data files placed outside this package.
    # See: http://docs.python.org/3.4/distutils/setupscript.html
    # format:
    #   [('target', ['list', 'of', 'files'])]
    # where target is sys.prefix/<target>
    data_files = [],

    # non zip-safe (never tested it)
    zip_safe = False,
)
