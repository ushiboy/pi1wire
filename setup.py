#!/usr/bin/env python3
from setuptools import setup
from setuptools.command.test import test

class PyTest(test):

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pi1wire',
    version='0.3.0',
    author='ushiboy',
    license='MIT',
    license_files = ('LICENSE.txt',),
    description='1Wire Sensor Library for Raspberry PI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ushiboy/pi1wire',
    packages=['pi1wire'],
    package_data={
        'pi1wire': ['py.typed'],
    },
    test_suite='tests',
    python_requires='>=3.7',
    tests_require=[
        'pytest'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux'
    ],
    cmdclass={'test': PyTest}
)
