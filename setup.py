import setuptools

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='period',
    version='0.0.1',
    author='Breitburg Elias',
    author_email='contact@breitburg.me',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/breitburg/period',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
