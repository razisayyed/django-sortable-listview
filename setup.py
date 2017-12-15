import os
from setuptools import setup

install_requires = [
    'django>=1.8',
]

try:
    from collections import OrderedDict
except ImportError:
    # add backport to list of required modules
    install_requires.append('ordereddict')

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.md')).read()
LICENSE = open(os.path.join(os.path.dirname(__file__), 'LICENSE.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sortable-listview',
    version='0.43',
    packages=['sortable_listview'],
    include_package_data=True,
    license=LICENSE,
    description='An extension of django\'s ListView that provides sorting',
    long_description=README + CHANGELOG,
    url='https://github.com/aptivate/django-sortable-listview',
    author='Aptivate',
    author_email='info@aptivate.org',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='tests.runtests.runtests'
)
