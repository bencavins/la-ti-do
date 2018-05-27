from setuptools import setup, find_packages

setup(
    name='music',
    version='0.0.0',
    author='Ben Cavins',
    author_email='bencavins@gmail.com',
    packages=find_packages(exclude=('tests', 'docs'))
)
