from setuptools import find_packages, setup


setup(
    name="stf_tools",
    version="0.0.1",
    author= "Victor Emenike",
    author_email='victor.emenike@uni-heidelberg.de',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description='Sequence-to-function (stf) tools: a collection of functions for sequence-to-function modelling',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    install_requires=[
        "joblib >= 1.4.2",
        "logomaker  >= 0.8.7",
        "numpy >= 1.14.2",
        "torch >= 1.9.0",
        "pandas >= 2.2.3",
        "scikit-learn >=1.6.1",
        "seaborn >= 0.13.2",
        "scipy >= 1.13.1",
        "numpy >= 2.0.1",
        "anndata >= 0.10.9",
        "gReLU >= 1.0.5",
        "matplotlib >=3.9.4",

],
)