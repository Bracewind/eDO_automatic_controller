#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['edocontroller', 'tests', 'example']
d['package_dir'] = {'': 'src'}
d['requires'] = ['getkey', 'numpy', 'numpy-quaternion']
# TODO Make catkin_make able to fetch getkey by itself?
setup(**d)
