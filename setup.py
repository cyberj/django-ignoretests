#!/usr/bin/env python
import sys, os

from setuptools import setup, find_packages

version = '0.3'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='django-ignoretests',
    version=version,
    description="Ignore tests of given django apps",
    long_description=README + '\nChangelog\n---------\n\n' +  CHANGES,
    classifiers=[
     "Programming Language :: Python",
     "Framework :: Django",
     "License :: OSI Approved :: MIT License",
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Johan Charpentier',
    author_email='cyberj@arcagenis.org',
    url='https://github.com/cyberj/django-ignoretests',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
    )
