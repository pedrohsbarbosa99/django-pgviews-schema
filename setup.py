from __future__ import absolute_import, print_function, unicode_literals

from os.path import isfile

from setuptools import setup, find_packages


if isfile("README.md"):
    LONG_DESCRIPTION = open("README.md").read()
else:
    LONG_DESCRIPTION = ""


setup(
    name="django-pgviews-schema",
    version="0.0.2",
    description="Create and manage Postgres SQL Views in Django",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Mikuláš Poul",
    author_email="git@mikulaspoul.cz",
    license="Public Domain",
    packages=find_packages(),
    url="https://github.com/pedrohsbarbosa99/django-pgviews-schema",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
    ],
)
