import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hmip",
    version="0.0.1",
    author="Mathilde Badoual",
    author_email="mathilde.badoual@berkeley.edu",
    description="Solver for large scale nonlinear mixed integer problems.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathildebadoual/Hopfield-NLMIP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)