#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:
#
# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

data = dict(
    name='python-datetime-tz',
    version='0.2',
    author='Tim Ansell',
    author_email='mithro@mithis.com',
    url='http://github.com/mithro/python-datetime-tz',
    description="""\
A drop in replacement for Python's datetime module which cares deeply about timezones.
""",
    license="License :: OSI Approved :: Apache Software License",
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Internationalization",
    ],
    packages=['datetime_tz'],
    install_requires=[],
    py_modules=['datetime_tz','datetime_tz.pytz_abbr'],
    test_suite='tests',
)

if sys.version[:3] < '3.0':
    data['install_requires'].append('pytz >= 2007g')
    data['install_requires'].append('python-dateutil >= 1.4, < 2.0')
else:
    data['install_requires'].append('pytz >= 2011g')
    data['install_requires'].append('python-dateutil >= 2.0')

setup(**data)
