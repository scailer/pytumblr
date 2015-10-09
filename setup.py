#!/usr/bin/env python

from setuptools import setup

setup(

    name="PyTumblr",
    version="0.0.6",
    description="A Python API v2 wrapper for Tumblr",
    author="John Bunting",
    author_email="johnb@tumblr.com",
    url="https://github.com/tumblr/pytumblr",
    packages = ['pytumblr'],
    license = "LICENSE",

    test_suite='nose.collector',

    install_requires = [
        'future',
        'requests-oauthlib',
    ],

    tests_require=[
        'httpretty',
        'nose',
        'nose-cov',
        'mock'
    ]

)
