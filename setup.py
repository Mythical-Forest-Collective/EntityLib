import setuptools

# Load the long_description from README.md
with open("README.md", "r") as fi:
    long_description = fi.read()

setuptools.setup(
    name="EntityLib",
    version="1.0.0",
    author="Mythical Forest Collective",
    description="A very bad package that is intended to help you make basic entity objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mythical-Forest-Collective/EntityLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
