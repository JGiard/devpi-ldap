import os

from setuptools import setup


def get_version(path):
    fn = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        path, "__init__.py")
    with open(fn) as f:
        for line in f:
            if '__version__' in line:
                parts = line.split("=")
                return parts[1].split("'")[1]


setup(
    name="devpi-ldap",
    version=get_version("devpi_ldap"),
    entry_points={
        'devpi_server': [
            "devpi-ldap = devpi_ldap.main"]},
    install_requires=[
        'devpi-server>=2.0.0',
        'ldap3>=0.9.8.6'],
    packages=['devpi_ldap'],
)
