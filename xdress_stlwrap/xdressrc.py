package = 'xdress_stlwrap'     # top-level python package name
packagedir = 'xdress_stlwrap'  # location of the python package
sourcedir = 'src'      # location of C/C++ source

stlcontainers = [
    ('vector', 'str'),
    ('set', 'uint'),
    ('map', 'int', 'float'),
    ]

# will be used later, but need to be present now
classes = []
functions = []
