#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="Python_modules",
    version="0.1.0",
    license="Apache license 2.0",
    author="Promobot",
    url="promo-bot.ru",
    project_urls={
        "Documentation": "https://promo-bot.ru",
        "Source Code": "https://github.com/Promobot-education",
    },
    description="Python modules to communicate with Promobot servos and range sensors",
    python_requires=">=2.7",
    py_modules=["Ranger","Servo","modbus_io"],
)
