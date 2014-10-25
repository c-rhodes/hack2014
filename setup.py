# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import hack2014
version = hack2014.__version__

setup(
    name='hack2014',
    version=version,
    author='',
    author_email='rhodes.cullen@gmail.com',
    packages=[
        'hack2014',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['hack2014/manage.py'],
)