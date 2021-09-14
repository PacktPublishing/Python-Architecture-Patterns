import setuptools
from Cython.Build import cythonize
from distutils.extension import Extension

extensions = [
    Extension("wheel_package_compiled", ["src/wheel_package_compiled.pyx"]),
]

with open('README') as readme:
    description = readme.read()


setuptools.setup(
    name='wheel-package-compiled',
    version='0.0.1',
    author='you',
    author_email='me@you.com',
    description='an example of a package',
    url='http://site.com',
    long_description=description,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    ext_modules=cythonize(extensions),
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.9',
)
