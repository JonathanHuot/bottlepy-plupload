import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="plupload",
    version="1.0",
    author="Jonathan Huot",
    author_email="jonathan.huot@gmail.com",
    description=("use plupload javascript library with python web apps based on bottlepy"),
    license="MIT",
    keywords="bottle web wsgi js plupload",
    url="https://github.com/JonathanHuot/bottlepy-plupload",
    packages=['plupload'],
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Framework :: Bottle',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
