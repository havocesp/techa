from setuptools import find_packages, setup

from techa import __version__, __author__, __package__, __license__, __dependencies__

setup(
    name=__package__,
    version=f'v{__version__}',
    requires=__dependencies__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={__package__: __package__},
    url= f'https://github.com/havocesp/{__package__}',
    license=__license__,
    author=__author__,
    author_email='10012416+havocesp@users.noreply.github.com',
    description=__package__.upper() + ': Technical Analysis Library',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Open source library with some useful routines.',
        f'License :: OSI Approved :: {__license__} License',        
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ], install_requires=__dependencies__ + ['finta']
)
