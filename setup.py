from setuptools import setup, find_packages
from pkg_resources import parse_requirements

with open('requirements.txt') as f:
    requirements = [str(req) for req in parse_requirements(f)]

setup(
    name='TP7_bloc2',
    version='0.1.0',
    author='Florian',
    author_email='jordany.florian@gmail.com',
    description='Partie TP7_bloc2 du TP 7 fil rouge',
    packages=find_packages(),
    install_requires=requirements,
)
