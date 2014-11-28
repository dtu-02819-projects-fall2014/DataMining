import os
import re
from setuptools import setup

PACKAGE_NAME = 'redditanalysis'

INIT = open(os.path.join(os.path.dirname(__file__), PACKAGE_NAME,
                         '__init__.py')).read()
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
VERSION = re.search("__version__ = '([^']+)'", INIT).group(1)

setup(name=PACKAGE_NAME,
      author='Jeppe de Lange and Niclas Bach Nielsen',
      author_email='blank@blank.com',
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'],
      description=('A tool to read reddit comments to analyze and graph them'),
      entry_points={'console_scripts': ['word_freqs={0}:main'
                                        .format(PACKAGE_NAME), ]},
      install_requires=['praw>=2.1.19'],
      license='GPLv3',
      long_description=README,
      packages=[PACKAGE_NAME],
      package_data={PACKAGE_NAME: ['redditanalysis/*.csv']},
      test_suite='tests',
      url='https://github.com/jeppedl/DataMining',
      version=VERSION,
      zip_safe = False)