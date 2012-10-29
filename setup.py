# -*- coding: utf-8 -*-
from setuptools import setup


requires = ('pync==1.1', 'requests==0.14.1')
packages = ('peekaboo',)

setup(
    name='Peekaboo',
    version='0.1',
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

