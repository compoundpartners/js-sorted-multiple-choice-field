# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from sortedm2m_filter_horizontal_widget import __version__


setup(
    name='js-sorted-multiple-choice-field',
    version=__version__,
    description=open('README.rst').read(),
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
