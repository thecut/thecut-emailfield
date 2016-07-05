from __future__ import print_function
import codecs
import io
import os
from thecut.emailfield import __version__
from setuptools import setup, find_packages
import sys
from sys import version_info as PYTHON_VERSION
from version import get_git_version


install_requires = ['sphinx_rtd_theme>=0.1.10a0']

if PYTHON_VERSION < (3,):
    install_requires.append('dnspython>=1.11.1,<2')
else:
    install_requires.append('dnspython3>=1.11.1,<2')


here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        filename = os.path.join(here, os.path.join('docs', filename))
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst', 'HISTORY.rst')

setup(
    # General information
    name='thecut-emailfield',
    version=__version__,

    # Packaging
    packages=find_packages(exclude=['docs']),
    namespace_packages=['thecut'],
    include_package_data=True,

    # Dependencies
    install_requires=install_requires,

    # Author information
    author='The Cut',
    author_email='development@thecut.net.au',

    # Additional information
    url='https://projects.thecut.net.au/projects/thecut-emailfield',
    license='Apache Software License 2.0',
    description=('A Django email field which validates by checking for an MX '
                 'record on the domain.'),
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ],
)
