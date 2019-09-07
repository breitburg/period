from setuptools import setup, find_packages
from pathlib import Path
from period.core.version import __version__

setup(
    name='period',
    version=__version__,
    author='Breitburg Elias',
    author_email='contact@breitburg.me',
    long_description=open(str(Path(__file__).resolve().parent.joinpath('readme.md')), 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url='https://github.com/getperiod/framework',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open(str(Path(__file__).resolve().parent.joinpath('requirements.txt')), 'r').read().split('\n'),
    dependency_links=['git+ssh://git@github.com/getperiod/factory.git']
)
