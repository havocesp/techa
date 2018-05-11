from setuptools import find_packages, setup


setup(
        name='techa',
        version='v0.0.5',
        requires=['pandas'],
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        package_dir={'techa': 'techa'},
        url='http://github.com/havocesp/techa',
        license='MIT',
        author='Daniel J. Umpierrez',
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
        ], install_requires=['pandas']
)
