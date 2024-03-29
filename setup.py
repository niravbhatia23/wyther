try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Wyther',
    version='0.1.4',
    author='Nirav Bhatia',
    packages=['wyther'],
    url='https://github.com/niravb1992/Wyther',
    license='LICENSE.txt',
    description='Python module to get the temperature of a place using Yahoo Weather API',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.0.1",
    ],
)
