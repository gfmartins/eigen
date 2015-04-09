import os
from Cython.Build import cythonize
from setuptools import setup, Extension

# ----------------------------------------------------------------------------
# Eigen sources
# ----------------------------------------------------------------------------
eigen = []
for root, dirnames, filenames in os.walk('eigen', followlinks=True):
    root = root.lstrip(os.path.join('eigen',''))
    eigen.extend((os.path.join(root, filename) for filename in filenames))

extensions = [
    Extension('test',
        sources = ['tests/test.pyx'],
        include_dirs = ['eigen'],
        extra_compile_args = ['-std=c++11'],
        language = 'c++'
    )
]


# ----------------------------------------------------------------------------
# Eigen
# ----------------------------------------------------------------------------
setup(name = 'Eigen',
    version = '0.1',
    description = 'Interface to Eigen C++ template library',
    long_description = open('README.md').read(),
    keywords = 'Eigen, C++, template, math, BLAS, cython',
    url = 'https://github.com/hbristow/eigen/',
    author = 'Hilton Bristow',
    author_email = 'hilton.bristow+eigen@gmail.com',
    license = 'GPL',
    packages = ['eigen'],
    package_data = {
        'eigen': eigen
    },
    install_requires = [
        'cython'
    ],
    ext_modules = cythonize(extensions),
    test_suite='tests',
    zip_safe=False)
