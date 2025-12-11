#!/usr/bin/env python3
"""
Setup script for HexLang
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hexlang",
    version="1.0.0",
    author="HexLang Contributors",
    author_email="",
    description="A programming language for humans who are tired of semicolons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HexCodeLang/hexlang",
    py_modules=["hexlang"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "hexlang=hexlang:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["examples/*.hexlang", "docs/*.md"],
    },
    keywords="programming-language interpreter compiler hexlang",
    project_urls={
        "Bug Reports": "https://github.com/HexCodeLang/hexlang/issues",
        "Source": "https://github.com/HexCodeLang/hexlang",
    },
)
