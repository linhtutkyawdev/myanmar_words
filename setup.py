from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="myanmar_words",
    version="1.0.0",
    author="Lin Htut Kyaw",
    author_email="linhtutkyaw.dev@gmail.com",
    description="A Python library for working with Myanmar words and sentences.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linhtutkyawdev/myanmar_words",
    packages=find_packages(),
    package_data={'myanmar_words': ['data/*.json']},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
)
