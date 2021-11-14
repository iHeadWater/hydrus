"""Setup script for realpython-reader"""

# Standard library imports
import pathlib
import io
import os

# Third party imports
from setuptools import setup

DESCRIPTION = "Read the latest Real Python tutorials"
# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
try:
    with io.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
        README = '\n' + f.read()
except FileNotFoundError:
    README = DESCRIPTION

# This call to setup() does all the work
setup(
    name="realpython-reader",
    version="1.0.0",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)
