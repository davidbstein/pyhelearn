import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhelearn-STEIN", # Replace with your own username
    version="0.0.1",
    author="David Stein",
    author_email="pyhelearn@davidbstein.com",
    description="FHE ML tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidbstein/pyhelearn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
