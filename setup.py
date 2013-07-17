# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='terrikon',
    version='0.0.1',
    description='web application for dynamic email generation',
    long_description=readme,
    author='Chris MacDonald',
    author_email='cmac1000@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

