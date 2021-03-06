import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'mcfly/_version.py')) as versionpy:
    exec(versionpy.read())

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = "mcfly",
    version = __version__,
    description = ("Deep learning for time series data"),
    license = "Apache 2.0",
    keywords = "Python",
    url = "https://github.com/NLeSC/mcfly",
    packages = find_packages(),
    install_requires=required,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
)
