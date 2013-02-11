#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
       scripts=['nodes/image_display.py',
                'nodes/movie_player.py',
                'nodes/volume_controller.py'],
       packages=['media_player'],
       package_dir={'': 'src'}
       )

setup(**d)
