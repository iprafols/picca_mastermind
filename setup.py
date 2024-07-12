from setuptools import setup, find_packages
import os

setup(
    name="picca_mastermind",
    version="0.1.0",
    packages=find_packages(include=["picca_mastermind", "picca_mastermind.*"]),
    install_requires=[
        "qsonic @ file://localhost/" + os.path.abspath("picca_mastermind/qsonic/py/qsonic"),
        "vega @ file://localhost/" + os.path.abspath("picca_mastermind/vega/vega"),
    ],
)
