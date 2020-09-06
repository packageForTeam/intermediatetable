from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="intermediatetable",
    version="0.0.1",
    author="Harsh Agrawal",
    author_email="dbgoyal31@gmail.com",
    description="A package to modify INT tables.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/packageForTeam/intermediatetable/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
