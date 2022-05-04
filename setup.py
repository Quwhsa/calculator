import setuptools

setuptools.setup (
  include_package+data = True,
  name='cal01',
  version='1.0.0.',
  description='oss-dev my calculator',
  author='김태형'
  author_email='kth990923@gmail.com',
  url='https://github.com/Quwhsa/calculator/',
  install_requires=['pytest'],
  long_description='oss-dev my calc',
  long_description_content_type='text/markdown',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
)
