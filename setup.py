import os
import sys

from setuptools import find_packages, setup

# FIXME: Main module requires django to be present, so cannot run setup.py in
# clean environment.
# from django_filters import __version__
__version__ = "22.1"

f = open("README.rst")
readme = f.read()
f.close()

if sys.argv[-1] == "publish":
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (__version__, __version__))
    print("  git push --tags")
    sys.exit()

setup(
    name="django-filter",
    version=__version__,
    description=(
        "Django-filter is a reusable Django application for allowing"
        " users to filter querysets dynamically."
    ),
    long_description=readme,
    author="Osvaldo Molina",
    author_email="osvaldo.molina.128@gmail.com",
    url="https://github.com/osval-do/django-nosql-objects/tree/main",
    packages=find_packages(exclude=["tests*"]),
    project_urls={
        # "Documentation": "https://django-filter.readthedocs.io/en/main/",
        "Changelog": "https://github.com/osval-do/django-nosql-objects/blob/main/CHANGES.rst",
        "Bug Tracker": "https://github.com/osval-do/django-nosql-objects/issues",
        "Source Code": "https://github.com/osval-do/django-nosql-objects",
    },
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "Django>=3.2",
    ],
)