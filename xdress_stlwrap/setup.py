import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'src'), np.get_include()]

ext_modules = [
    Extension("xdress_stlwrap.xdress_extra_types", ["xdress_stlwrap/xdress_extra_types.pyx"], 
              include_dirs=incdirs, language="c++"),
    Extension("xdress_stlwrap.stlcontainers", ["xdress_stlwrap/stlcontainers.pyx"], 
              include_dirs=incdirs, language="c++"),
    ]

setup(
  name = 'xdress_stlwrap',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['xdress_stlwrap']
)
