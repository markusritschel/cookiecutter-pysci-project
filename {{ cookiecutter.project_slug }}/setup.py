from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='{{ cookiecutter.project_version }}',
    description='{{ cookiecutter.project_description }}',
    author='{{ cookiecutter.author }}',
    license='{{ cookiecutter.license }}'
)
