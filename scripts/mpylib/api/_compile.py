from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("_openmaya",  ["_openmaya.py"]),
    Extension("openmaya", ["openmaya.py"]),
]
setup(
    name = 'MPyNode',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)