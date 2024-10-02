from setuptools import setup, find_packages

setup(
    name='dummy_package',
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'prefect==2.20.4',
        'databricks-connect==14.*'
    ],
    entry_points={
        'console_scripts': [
            'dummy_package.module:main',
        ]
    }
)