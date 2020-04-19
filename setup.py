# !/usr/bin/env python3

import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# test dependencies
test_deps = [
    'pytest',
    'pytest-cov',
]
extras = {
    'test': test_deps,
}

# This call to setup() does all the work
setup(
    name="seqparser",
    version="1.1.2",
    description="Cli tool to find specific regular expression like email, ip adress, phone number, bitcoin adress ... in a file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/remiflavien1/seqparser",
    author="shadawck",
    author_email="hug211mire@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        'Topic :: Security',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Internet :: Log Analysis',
    ],
    packages=["seqparser"],
    package_data = {'seqparser': ['./*.txt']},
    include_package_data=True,
    install_requires=["docopt"],
    keywords='security, parser, forensic, analysis, sequence parser, regex',
    tests_require=test_deps,
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "seqparser=seqparser.__main__:main",
        ]
    },
)