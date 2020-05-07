#!/usr/bin/env python

from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='testMethod',
      version='1.0',
      description='Python Distribution Utilities',
      author='Geekshubs',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
     )
