#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    return '2.13.0'


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
