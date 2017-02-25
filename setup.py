#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


from persistiq import __str_version__, __author__


setup(
    name='persistiq',
    version=__str_version__,
    description='A simple python wrapper for the PersistIQ API',
    url='https://github.com/tizz98/persistiq',
    download_url='https://github.com/tizz98/persistiq/tarball/%s' % (
        __str_version__
    ),
    author=__author__,
    author_email='elijah@elijahwilson.me',
    license='MIT',
    packages=['persistiq'],
    keywords='persistiq api',
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'requests',
    ]
)
