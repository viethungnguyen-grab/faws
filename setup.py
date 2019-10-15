#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Viet Hung Nguyen",
    author_email='hvn@familug.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Fast, functional AWS lib bases on boto3",
    entry_points={
        'console_scripts': [
            'faws=faws.cli:main',
        ],
    },
    extras_require={
        'boto3': ['boto3>=1.9.15', 'botocore>=1.12.15'],
        'cli': ['Click>=6.0']
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='faws',
    name='faws',
    packages=find_packages(include=['faws']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hvnsweeting/faws',
    version='0.1.10',
    zip_safe=False,
)
