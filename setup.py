#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

if sys.platform == 'darwin':
    lxml = "lxml<2.4"
else:
    lxml = "lxml"

setup(
    name="python-readability",
    author="Miguel Galves",
    author_email="mgalves@gmail.com",
    version="0.3.0.2",
    description="fast python port of arc90's readability tool",
    test_suite = "tests.test_article_only",
    long_description=open("README").read(),
    license="Apache License 2.0",
    url="http://github.com/mgalves/python-readability",
    packages=['readability'],
    install_requires=[
        "chardet",
        lxml
        ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
)
