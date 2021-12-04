import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="batchify",
    version="0.0.1",
    author="Michael Arcidiacono",
    author_email="",
    description="batchify anything",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mixarcid/batchify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
