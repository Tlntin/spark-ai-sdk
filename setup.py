# coding=utf-8
from setuptools import setup
import sys


if sys.version_info < (3, 5):
    print('Glances requires at least Python 3.5 to run.')
    sys.exit(1)

setup(
    author="Tlntin",
    description="python api for XunFei (iFLYTEK) Spark AI",
    url="https://github.com/Tlntin/spark_api",
    name="spark_ai_sdk",
    version="0.0.1",
    packages=['spark_ai_sdk'],
    install_requires=[
        "websocket_client>=1.6.1",
    ],
    entry_points={
        'console_scripts': []
    },
)