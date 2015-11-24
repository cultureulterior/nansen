import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nansen",
    version = "0.1.0",
    author = "Samuel Kleiner",
    author_email = "sam@firstbanco.com",
    description = ("Consul host & docker tree"),
    license = "GPL",
    keywords = "consul docker ssh",
    install_requires = ['npyscreen'],
    long_description=read('README.md'),
    scripts=['nansen'],
    classifiers=[
        "Topic :: Utilities",
    ],
)
