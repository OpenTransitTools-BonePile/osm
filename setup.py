import os
import sys
import setuptools
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'simplejson'
]

#
# eggs that you need if you're running a version of python lower than 2.7
#
if sys.version_info[:2] < (2, 7):
    requires.extend(['argparse>=1.2.1', 'unittest2>=0.5.1'])

#
# eggs you need for development, but not production
#
dev_extras = (
    'zc.buildout',
    'coverage>=3.5.2',
    'fabric>=1.4.3',
    'zest.releaser>=3.37',
    'nose'
)

setup(
    name='ott.osm',
    version='0.1.0',
    description='Open Transit Tools - OSM Tools (Python)',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
    ],
    author="Open Transit Tools",
    author_email="info@opentransittools.com",
    dependency_links=('http://opentransittools.com',),
    license="Mozilla-derived (http://opentransittools.com)",
    url='http://opentransittools.com',
    keywords='ott, otp, view, transit, osm',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require=dict(dev=dev_extras),
    tests_require=requires,
    test_suite="ott.osm",
    entry_points="""\
        [paste.app_factory]
        main = ott.view.pyramid.config:main
    """,
)
