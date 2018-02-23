#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# # or more contributor license agreements.  See the NOTICE file
# # distributed with this work for additional information
# # regarding copyright ownership.  The ASF licenses this file
# # to you under the Apache License, Version 2.0 (the
# # "License"); you may not use this file except in compliance
# # with the License.  You may obtain a copy of the License at
# #
# #   http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing,
# # software distributed under the License is distributed on an
# # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# # KIND, either express or implied.  See the License for the
# # specific language governing permissions and limitations
# # under the License.

from __future__ import print_function, division

import pip
import sys

from setuptools.command.test import test as TestCommand
from setuptools import find_packages
from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main("%s tests" % " ".join(self.test_args))
        sys.exit(errno)


def requirements():
    return [str(ir.req) for ir in parse_requirements('requirements.txt',
                                                     session=False)]


def get_version():
    return '2.10.0a2'


setup(
    name='impala_shell',
    version=get_version(),
    description='Impala Shell.',
    long_description=open('README.md').read(),
    author='Impala Dev Team',
    author_email='dev@cloudera.com',
    py_modules=['impala_shell',
                'impala_client',
                'impala_shell_config_defaults',
                'option_parser',
                'shell_output',
                'TSSLSocketWithWildcardSAN'],
    packages=find_packages('impala_shell', exclude=["tests"]),
    package_dir={'': 'impala_shell'},
    include_package_data=True,
    install_requires=requirements(),
    tests_require=["pytest"],
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
            'impala-shell = impala_shell:main'
        ]
    }
)
