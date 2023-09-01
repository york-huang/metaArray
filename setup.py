#!/usr/bin/env python

from setuptools import setup


#
# Most setuptools configure is moved to pyproject.toml according to
# the new Python packaging best practice.
#

setup(
    long_description="""
    Wrapper for combining numpy ndarrays with meta information. Also has useful utilities;
    for example, reading in data files from PZFlex, binary data from oscilloscopes, talking
    to impedance analysers, etc.""",
 )


