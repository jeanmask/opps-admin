#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='opps-admin',
    version='0.1',
    description='Opps Admin, drop-in replacement of Django admin comes with lots of goodies, fully extensible with plugin support, pretty UI based on Twitter Bootstrap.',
    long_description=open('README.rst').read(),
    author='sshwsfc',
    url='http://www.oppsproject.org',
    download_url='http://github.com/opps/opps-admin/tarball/master',
    packages=find_packages(exclude=('doc', 'docs',)),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'opps>=0.2',
        'xlwt',
        'django-crispy-forms>=1.2.3',
    ],
    zip_safe=True,
    keywords=['admin', 'django', 'xadmin', 'bootstrap', 'opps', 'opps-admin'],
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
