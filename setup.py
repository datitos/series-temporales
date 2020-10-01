import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mendotimeseries",
    version="0.0.1",
    author="Mendo Team",
    author_email="pm@mendoteam.com",
    description="A time series prediction package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datitos/package",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas>=0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
        'scikit-learn>=0.22.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
