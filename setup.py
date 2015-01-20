from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-customapi',
    version=version,
    description="Attempt to add another route to the API.",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Milo',
    author_email='milo.thurston@oerc.ox.ac.uk',
    url='http://tess.oerc.ox.ac.uk',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.customapi'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        customapi=ckanext.customapi.plugin:CustomAPIPlugin
    ''',
)
