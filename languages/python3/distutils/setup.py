#!/usr/bin/env python

from distutils.core import setup

setup(name='ExamplePackage',
      version='0.1.0',
      description='Example package python',
      author='Jean-Charles Naud',
      author_email='jcnaud@python.net',
      url='https://github.com/jcnaud',
      license='LICENSE.txt',
      packages=['distutils', 'distutils.command'],
      scripts=['scripts/run'],
      long_description=open('README.txt').read(),
      install_requires=[
          "PyYAML"
      ],
      )
