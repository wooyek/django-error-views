#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import os
import re
import uuid
from glob import glob
from os.path import basename, splitext

try:  # for pip >= 10
    # noinspection PyProtectedMember,PyPackageRequirements
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    # noinspection PyPackageRequirements
    from pip.req import parse_requirements

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def requirements(path):
    items = parse_requirements(path, session=uuid.uuid1())
    return [";".join((str(r.req), str(r.markers))) if r.markers else str(r.req) for r in items]


install_requires = requirements(os.path.join(os.path.dirname(__file__), "requirements.txt"))


def get_version(*file_paths):
    """Retrieves the version from path"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    print("Looking for version in: {}".format(filename))
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("src", "website", "__init__.py")

setup(
    name='django-error-views-example',
    version=version,
    description="""Example app for django-error-views""",
    long_description="""This is an example project that should not be published or installed""",
    author="Janusz Skonieczny",
    author_email='js+pypi@bravelabs.pl',
    url='https://github.com/wooyek/django-error-views',
    packages=find_packages('src', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    exclude_package_data={
        '': ['test*.py', 'tests/*.env', '**/tests.py'],
    },
    python_requires='>=2.7',
    install_requires=install_requires,
    extras_require={
        'factories': ['factory-boy'],
    },
    zip_safe=False,
    keywords='django-error-views',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='runtests.run_tests',
    tests_require=['pytest', 'pytest-django'],
    # https://docs.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
    setup_requires=['pytest-runner'],
)
