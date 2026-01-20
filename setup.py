#!/usr/bin/env python3
"""
Setup script for gpapis.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read version from __init__.py
version = ""
with open(Path(__file__).parent / "gpapis" / "__init__.py", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"')
            break

# Read README.md for long description
long_description = ""
if (Path(__file__).parent / "README.md").exists():
    with open(Path(__file__).parent / "README.md", "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="gpapis",
    version=version,
    description="GlobalPlatform API Manager - Helps configure and access GlobalPlatform API specifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ibaibing",
    author_email="ibaibing@outlook.com",
    url="https://github.com/ibaibing/gpapis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "gpapis = gpapis.cli:main",
        ],
    },
    keywords="globalplatform, api, javacard, smartcard",
    license="MIT",
    project_urls={
        "Source": "https://github.com/ibaibing/gpapis",
        "Bug Reports": "https://github.com/ibaibing/gpapis/issues",
        "Documentation": "https://github.com/ibaibing/gpapis",
    },
)