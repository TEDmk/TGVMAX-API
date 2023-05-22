import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'requests==2.31.0',
    ]

tests_require = [
    'pytest',
    'pycov'
    ]

setup(name='TGVMAX-API',
      version='0.0.0',
      description='TGMAX API to list and book TGVMax',
      packages=['tgvmax_api'],
      package_data={
        '': ['*.json']
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extra_requires={
        'test': tests_require
      }
      )