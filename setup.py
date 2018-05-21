from setuptools import find_packages, setup

from techa import __version__, __author__, __package__

setup(
        name='techa',
    version='v' + __version__,
        requires=['pandas'],
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        package_dir={'techa': 'techa'},
    url='http://github.com/havocesp/' + __package__,
        license='MIT',
    author=__author__,
        author_email='',
        description='TECHA: Technical Analysis Library',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Open source library with some useful routines.',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
        ], install_requires=['pandas', 'finta']
)
