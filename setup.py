try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Hackbright Week 1 Assessment',
    'author': 'Siena Aguayo',
    'url': 'URL',
    'author_email': 'siena.aguayo@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['skills1'],
    'scripts': [],
    'name': 'Week 1 Assessment'
}

setup(**config)