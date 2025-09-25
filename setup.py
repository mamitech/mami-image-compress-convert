#!/usr/bin/env python3
"""Setup script for Image Compressor & Converter."""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

# Read requirements
def read_requirements():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='mami-image-compress-convert',
    version='1.0.0',
    description='A powerful, user-friendly terminal application for image compression and format conversion',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Mami Team',
    author_email='engineering@mamiteam.com',
    url='https://github.com/mamitech/mami-image-compress-convert',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],

    keywords='image compression conversion jpeg png webp batch processing',

    packages=find_packages(),
    py_modules=['app'],

    python_requires='>=3.7',
    install_requires=read_requirements(),

    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
            'pre-commit>=2.20',
        ],
    },

    entry_points={
        'console_scripts': [
            'mami-image=app:main',
        ],
    },

    scripts=['mami-image'],

    include_package_data=True,
    package_data={
        '': ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'requirements.txt'],
    },

    project_urls={
        'Bug Reports': 'https://github.com/mamitech/mami-image-compress-convert/issues',
        'Source': 'https://github.com/mamitech/mami-image-compress-convert',
        'Documentation': 'https://github.com/mamitech/mami-image-compress-convert#readme',
        'Contributing': 'https://github.com/mamitech/mami-image-compress-convert/blob/main/CONTRIBUTING.md',
    },
)
