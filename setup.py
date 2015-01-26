from setuptools import setup

VERSION = '0.7.0'

setup(
    name='django-react',
    version=VERSION,
    packages=['django_react'],
    package_data={
        'django_react': [
            'render.js',
            'package.json',
            'templates/django_react/*.html',
            'tests/*.py',
            'tests/test_components/*.jsx',
            'tests/test_components/*.js',
        ]
    },
    install_requires=[
        'django',
        'django-node == 2.2.1',
        'django-webpack == 2.0.2',
    ],
    description='Render and bundle React components from a Django application',
    long_description='Documentation at https://github.com/markfinger/django-react',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/django-react',
)