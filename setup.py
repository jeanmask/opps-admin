#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='opps-admin',
    version='0.1',
    description='Opps Admin, drop-in replacement of Django admin and widgets for Opps CMS.',
    long_description=open('README.rst').read(),
    author='YACOWS',
    url='http://www.oppsproject.org',
    download_url='http://github.com/opps/opps-admin/tarball/master',
    packages=find_packages(exclude=('doc', 'docs',)),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'opps>=0.2',
    ],
    zip_safe=True,
    keywords=['admin', 'django', 'opps', 'opps-admin'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
