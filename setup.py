from setuptools import setup
import os

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

dir_setup = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_setup, 'liepack', 'release.py')) as f:
    exec(f.read())

modules = ['liepack.liealgebras',
           'liepack.liegroups']

tests = ['liepack.liealgebras.tests',
         'liepack.liegroups.tests']

setup(
    name='liepack',
    version=__version__,
    description='A NumPy-based library for Lie algebras and their associated groups.',
    long_description='A NumPy-based library for Lie algebras and their associated groups.',
    author='Michael Sparapany',
    author_email='msparapa@purdue.edu',
    license='',
    url='https://github.com/msparapa/liepack',
    packages=['liepack'] + modules + tests,
    py_modules=['liepack'],
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'),
    install_requires=requirements,
)
