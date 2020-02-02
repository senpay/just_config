import os
from setuptools import setup

from just_config import version


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='just-config',
    version=version.VERSION,
    author='Alexander Pushkarev',
    author_email='alexspush@gmail.com',
    description='Minimalistic library to handle configuration for the application',
    license='MIT',
    url='http://packages.python.org/just_config',
    packages=['just_config'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown'
)
