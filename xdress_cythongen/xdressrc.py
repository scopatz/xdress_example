package = 'xdress_cythongen'     # top-level python package name
packagedir = 'xdress_cythongen'  # location of the python package
sourcedir = 'src'      # location of C/C++ source

classes = [
    ('A', 'hoover'),
    ('B', 'hoover', 'hoover_b'),
    ]

functions = [('do_nothing_ab', 'hoover')]
