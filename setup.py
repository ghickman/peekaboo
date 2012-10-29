# -*- coding: utf-8 -*-
from setuptools import setup

import peekaboo


requires = ('pync==1.1', 'requests==0.14.1')
packages = ('peekaboo',)

setup(
    name='Peekaboo',
    version=peekaboo.__version__,
    description='Rename tv show files using online databases',
    long_description=open('README.rst').read(),
    author='George Hickman',
    author_email='george@ghickman.co.uk',
    url='http://tvrenamr.info',
    license=open('LICENSE').read(),
    py_modules=('peekaboo',),
    entry_points={'console_scripts': ['peekaboo=peekaboo:run']},
    install_requires=requires
)

