from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="aariz",
      author_email="aariz120@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )