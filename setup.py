from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    python_requires='>=3',
    name='ndarrays4j',
    version='1.0',
    long_description=long_description,
    license="MIT",
    author='Charles Gobber',
    author_email='charles26f@gmail.com',
    description='A python package to share memory between arrays4j (Java) with numpy (Python)',
    packages=['ndarrays4j'],
    install_requires=['numpy','pyjnius']
)