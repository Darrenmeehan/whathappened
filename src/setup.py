#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="whathappened",
        version="1.0.0",
        description="Easily see what is happening in your AWS Account",
        entry_points={"console_scripts": ["whathappened = whathappened.core.main"]},
        packages=setuptools.find_packages(include="whathappened/*"),
    )
