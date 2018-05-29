from setuptools import find_packages, setup

from techa import __version__, __author__, __package__, __license__, __dependencies__

setup(
    name=__package__,
    version='v' + __version__,
    requires=__dependencies__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={__package__: __package__},
    url='http://github.com/havocesp/' + __package__,
    license=__license__,
    author=__author__,
    author_email='',
    description=__package__.upper() + ': Technical Analysis Library',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Open source library with some useful routines.',
        'License :: OSI Approved :: {} License'.format(__license__),
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ], install_requires=__dependencies__ + ['finta']
)
