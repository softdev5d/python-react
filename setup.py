from setuptools import setup

VERSION = '0.4.0'

setup(
    name='django-react',
    version=VERSION,
    packages=['django_react'],
    package_data={
        'django_react': [
            'render.js',
            'package.json',
            'tests/*.py',
            'tests/test_components/*.jsx',
            'tests/test_components/*.js',
        ]
    },
    install_requires=[
        'django',
        'django-node >= 2.0.1',
        'django-webpack >= 1.0.1',
    ],
    description='Django React',
    long_description=\
'''
Render and bundle React components from a Django application.

Documentation at https://github.com/markfinger/django-react
''',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/django-react',
)