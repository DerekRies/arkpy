from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Minimal Requirements for pip installs to work.
requires = ['enum34>=1.1.6']

setup(
    name='arkgamepy',
    version='0.1.3',
    description='A library for reading and writing the file formats of ARK: Survival Evolved',
    long_description=long_description,
    packages= ['arkpy'],
    # The project's main homepage.
    url='https://github.com/DerekRies/arkpy',
    download_url='',
    author='Derek Ries',
    author_email='iamderekries@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.2',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
    ],
    install_requires=requires,
    keywords=['ark', 'game', 'ark survival', 'ark survival evolved',
              '.ark', '.arkprofile', '.arktribe', '.arkcharactersetting',
              'reverse engineering', 'game files'],
)