from setuptools import setup, find_packages
from sys import version_info as PYTHON_VERSION
from version import get_git_version

install_requires = []

if PYTHON_VERSION < (3,):
    install_requires.append('dnspython>=1.11.1,<2')
else:
    install_requires.append('dnspython3>=1.11.1,<2')

setup(
    name='thecut-emailfield',
    author='The Cut',
    author_email='development@thecut.net.au',
    url='https://projects.thecut.net.au/projects/thecut-emailfield',
    namespace_packages=['thecut'],
    version=get_git_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
