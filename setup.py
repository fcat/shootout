import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'setuptools >= 1.2',
    'pyramid>=1.0, <1.3',
    'SQLAlchemy >= 0.8.1',
    'transaction == 1.4.1',
    'pyramid_chameleon == 0.1',
    'pyramid_tm > 0.6',
    'pyramid_debugtoolbar > 1.0.8',
    'pyramid_exclog > 0.6, <0.8',
    'zope.sqlalchemy >= 0.7.3, != 0.7.4, <0.8',
    'pyramid_simpleform >=0.6.1, <0.7, >=0.8, <1',
    'cryptacular',
    'waitress',
    'pycrypto',
    'WebTest == 2.0.10',
    ]

if sys.version_info[:3] < (2,5,0):
    raise RuntimeError('This application requires Python 2.6+')

setup(name='shootout',
      version='0.2.3',
      description='A generic idea discussion and rating app (Pyramid sample)',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Framework :: Pylons",
        "Framework :: BFG",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Carlos de la Guardia, Lukasz Fidosz",
      author_email="cguardia@yahoo.com, virhilo@gmail.com",
      url='http://pylons-devel@googlegroups.com',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      keywords='web wsgi bfg pyramid pylons example',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='shootout.tests',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = shootout:main
      [console_scripts]
      initialize_shootout_db = shootout.scripts.initializedb:main
      """,
      )

