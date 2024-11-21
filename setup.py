from setuptools import setup, find_packages

setup(
    name="libcli",
    version="1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["libcli=libcli.cli:main"]},
)
