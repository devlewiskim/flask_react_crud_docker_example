#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
    name='lewis_app',
    version='1.0',

    packages=['main'],
    platforms='any',
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'SQLAlchemy-serializer',
        'sqlalchemy-utils',
        'flask-migrate',
        'flask-script',
        'pyjwt',
        'jsonschema',
        'flask-restful'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
