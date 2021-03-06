#!/usr/bin/env python

import codecs
import re
from os import path

from setuptools import setup


VERSIONFILE = "aws_adfs/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = '([^']+)'"
mo = re.search(VSRE, verstrline, re.MULTILINE)
if mo:
    version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

tests_require = [
    'pytest',
    'mock',
    'coverage < 4',
]

setup(
    name='aws-adfs',
    version=version,
    description='AWS Cli authenticator via ADFS - small command-line tool '
                'to authenticate via ADFS and assume chosen role',
    long_description=codecs.open(
        path.join(path.abspath(path.dirname(__file__)), 'README.md'),
        mode='r',
        encoding='utf-8'
    ).read(),
    url='https://github.com/venth/aws-adfs',
    download_url='https://github.com/venth/aws-adfs/tarball/{}'.format(version),
    author='Venth',
    author_email='artur.krysiak.warszawa@gmail.com',
    maintainer='Venth',
    keywords='aws adfs console tool',
    packages=['aws_adfs'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],

    setup_requires=[
        'pytest-runner',
        'setuptools',
    ],
    install_requires=[
        'lxml',
        'click',
        'boto3',
        'requests',
        'configparser'
    ],

    tests_require=tests_require,
    extras_require={'test': tests_require},

    entry_points={
        'console_scripts': ['aws-adfs=aws_adfs.commands:cli']
    },
    include_package_data=True,
)
