#!/usr/bin/env python

from os.path import isdir
from setuptools import setup, find_namespace_packages
from shutil import rmtree

egg_info_dir = 'pytgbb.egg-info'
if isdir(egg_info_dir):
    rmtree(egg_info_dir)

setup(packages = find_namespace_packages(include=['pytgbb.*']))
