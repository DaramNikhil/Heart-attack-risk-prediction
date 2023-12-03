#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="daram nikhil",
    author_email='nikhildaram11@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="end to end heart attack risk prediction",
    entry_points={
        'console_scripts': [
            'heart_attack_risk_prediction=heart_attack_risk_prediction.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='heart_attack_risk_prediction',
    name='heart_attack_risk_prediction',
    packages=find_packages(include=['heart_attack_risk_prediction', 'heart_attack_risk_prediction.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/nikhil/heart_attack_risk_prediction',
    version='0.0.1',
    zip_safe=False,
)
