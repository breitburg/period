import setuptools

setuptools.setup(
    name='period',
    version='0.0.2',
    author='Breitburg Elias',
    author_email='contact@breitburg.me',
    long_description=open('readme.md', 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url='https://github.com/breitburg/period',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open('requirements.txt', 'r').read().split('\n')
)
