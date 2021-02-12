from setuptools import setup, find_packages

setup(
    name = "exchange_rate",
    author = "ksysiupeel",
    author_email = "ksysiupeel@protonmail.com",
    install_requires = ["requests"],
    version = "1.0",
    description = "Simple wrapper using exchangeratesapi.io",
    long_description = open("README.md").read(),
    url = "https://github.com/Ksysiupeel/Exchange-rate-in-python.git",
    packages = find_packages()
)