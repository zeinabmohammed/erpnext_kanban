# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
from ast import literal_eval

version = '0.0.1'
with open('requirements.txt') as r:
	install_requires = r.read().strip().split('\n')

setup(
	name='kanban',
	version=version,
	description='Kanban views for ERPNext',
	author='Alec Ruiz-Ramon',
	author_email='alec.ruizramon@me.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	include_package_data=True,
	install_requires=install_requires
)
