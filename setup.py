import codecs
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "release-please-python"
PACKAGES = ["release-please-python"]
DESCRIPTION = "this is a test package for packing python liberaries tutorial."
LONG_DESCRIPTION = read("README.md")
KEYWORDS = "python package"
AUTHOR = "pzhong"
AUTHOR_EMAIL = ""
VERSION = "0.0.1"
URL = " "
LICENSE = "MIT"


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    setup_requires=[
    ],
    install_requires=[
    ]
)
