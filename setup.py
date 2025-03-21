from setuptools import setup
from setuptools import find_packages

long_description= """
Text analysis tools for the Computers and the Humanities Course
"""

required = [
    "pandas",
    "statsmodels",
    "seaborn",
    "matplotlib",
    "scikit-learn"
]

setup(
    name="s2l",
    version="0.0.1",
    description="Sampling tools",
    long_description=long_description,
    author="Er Qi Yang",
    install_requires=required,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
)
