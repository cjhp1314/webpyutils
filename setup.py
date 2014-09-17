from setuptools import setup

setup(name='webpyutils',
    version='0.1',
    description='web.py utilities to build quick RESTful API Services',
    author='Jesse V. Yen',
    author_email='jesse@jads.com',
    url='https://github.com/jvy1106/webpyutils',
    install_requires=[
        'DBUtils',
        'web.py',
        'flup',
    ],  
    packages=[
        'webpyutils',
    ],  
)
