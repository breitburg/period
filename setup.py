from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='period',
    version='0.1.2',
    author='Breitburg Elias',
    author_email='contact@breitburg.me',
    long_description=open(str(Path(__file__).resolve().parent.joinpath('readme.md')), 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url='https://github.com/breitburg/period',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['period=period.cli:main'],
    },
    install_requires=open(str(Path(__file__).resolve().parent.joinpath('requirements.txt')), 'r').read().split('\n'),
    dependency_links=['git+ssh://git@github.com/getperiod/factory.git']
)
