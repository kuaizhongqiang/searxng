# SPDX-License-Identifier: AGPL-3.0-or-later
"""Installer for SearXNG-core package (AgentWebSearchingTool fork)."""

from setuptools import setup, find_packages

from searx.version import VERSION_TAG, GIT_URL

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f.readlines()]

setup(
    name='searxng-core',
    description="SearXNG-core: stripped metasearch engine for AgentWebSearchingTool",
    long_description=long_description,
    license="AGPL-3.0-or-later",
    author='SearXNG (forked by kuaizhongqiang)',
    python_requires=">=3.10",
    version=VERSION_TAG,
    keywords='metasearch searchengine search web http',
    url=GIT_URL,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    project_urls={"Code": GIT_URL},
    entry_points={
        'console_scripts': ['searxng-run = searx.webapp:run']
    },
    packages=find_packages(
        include=[
            'searx',
            'searx.*',
            'searx.*.*',
            'searx.*.*.*',
        ]
    ),
    package_data={
        'searx': [
            'settings.yml',
            '*.toml',
            '*.msg',
            'data/*.json',
            'data/*.txt',
            'data/*.ftz',
            'favicons/*.toml',
        ],
    },
    install_requires=requirements,
)
