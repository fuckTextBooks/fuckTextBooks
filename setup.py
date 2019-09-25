#!/usr/bin/env python

from distutils.core import setup
from webdriverdownloader import GeckoDriverDownloader

setup(name='FuckTextBooks',
      version='1.0',
      description='Auto download course materials for UofT students',
      packages=['distutils', 'bs4', 'libgenapi',
                'getpass', 'selenium', 'webdriverdownloader'],
      )

# Install geckodriver
gd = GeckoDriverDownloader()
gd.download_and_install()
