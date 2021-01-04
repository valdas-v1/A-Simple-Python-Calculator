import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculator-valdas-v1",
    version="0.0.1",
    author="valdas-v1",
    description="A simple python calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valdas-v1/turing_215_calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
