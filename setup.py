from setuptools import setup

setup(name='glassbrain',
      version='1.0',
      packages=['glassbrain', 'glassbrain.domain'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
      )