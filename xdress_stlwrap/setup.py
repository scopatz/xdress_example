import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd(), 'src'), np.get_include()]

ext_modules = [
    Extension("hello.xdress_extra_types", ["hello/xdress_extra_types.pyx"], 
              include_dirs=incdirs, language="c++"),
    Extension("hello.stlcontainers", ["hello/stlcontainers.pyx"], 
              include_dirs=incdirs, language="c++"),
    ]

setup(
  name = 'hello',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['hello']
)
