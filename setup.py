from setuptools import setup

with open("README.md", "r") as f:
  readme = f.read()

setup(
  name = 'madlibspy',
  packages = ['madlibspy'],
  version = '2.1',
  license='MIT',
  description = 'A library to create your own madlibs game!',
  author = 'Nemika',
  author_email = 'nemika@bytestobits.dev',
  url = 'https://github.com/Nemika-Haj/MadLibsPy',
  keywords = ['madlibspy', 'madlibs', 'py', 'python', 'game', 'madlibs.py'],
  long_description=readme,
  long_description_content_type="text/markdown",
  install_requires=[
          'requests',
          'Python.js'
      ],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9'
  ],
)