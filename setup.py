import setuptools

setuptools.setup (
  include_package+data = True,
  name='cal01',
  version='1.0.0.',
  description='oss-dev my calculator',
  author='κΉνν'
  author_email='kth990923@gmail.com',
  url="https://github.com/Quwhsa/calculator/",
  download_url = "https://github.com/Quwhsa/calculator/archive/refs/tags/v1.0.0.zip",
  install_requires=['pytest'],
  long_description='oss-dev my calc',
  long_description_content_type='text/markdown',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
)
