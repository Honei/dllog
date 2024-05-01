#!/usr/bin/env python3
# -*- coding:utf-8
"""
@time   ： 2024/5/1 11:22
@author ：xiongxinlei
@file   ：setup.py
"""


from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fr:
    readme = fr.read()

with open('LICENSE', 'r', encoding='utf-8') as fr:
    license = fr.read()



setup(name='dllog',
      version='0.0.1',
      description='dllog: Log tool for Deep Learning experiment logger, developed by xiongxinlei',
      long_description=readme,
      long_description_content_type='text/markdown',
      license='Apache license',
      python_requires='>=3.8',
      include_package_data=True,
      packages=find_packages())