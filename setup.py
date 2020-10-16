import os.path as path
from setuptools import setup, find_packages, dist
import sys

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(name='dxapi',
      version='6.0.8',
      packages=find_packages(),
      package_data={'dxapi': ['windows/x64/py27/*.pyd',
            'windows/x64/py36/*.pyd',
            'windows/x64/py37/*.pyd',
            'windows/x64/py38/*.pyd',
            'linux/x64/py27/*.so',
            'linux/x64/py36/*.so',
            'linux/x64/py37/*.so',
            'linux/x64/py38/*.so',
            'darwin/x64/py27/*.so',
            'darwin/x64/py36/*.so',
            'darwin/x64/py37/*.so',
            'darwin/x64/py38/*.so',
            'darwin/x64/py27/*.dylib',
            'darwin/x64/py36/*.dylib',
            'darwin/x64/py37/*.dylib',
            'darwin/x64/py38/*.dylib']},
      include_package_data=True,
      zip_safe=False,
      description='Python Timebase client API',
      long_description='Python Timebase client API',
      long_description_content_type='text/markdown',
      keywords='timebase, database',
      #url='',
      author='Raman Kisel',
      author_email='Raman_Kisel@epam.com',
      classifiers=[
          "Operating System :: Microsoft :: Windows",
          "Operating System :: POSIX :: Linux",
          "Operating System :: MacOS",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8"
      ],
      python_requires='>=2.7,!=2.8.*,!=2.9.*,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,<3.9',
      platforms=['Windows', 'Linux', 'MacOS']
)
