import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclear", # Replace with your own username
    version="1.0.7",
    author="Daniel Smith",
    author_email="daniel@waiora.com.au",
    description="A simple tool to clear the command line shell you are in",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PythonEuropa/pyclear",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)