from setuptools import setup, find_packages

setup(
    name = "greetings",
    version = "1.0",
    url = '',
    license = 'All Rights Reserve',
    description = "Trial to recipe making",
    author = 'Yona',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)

