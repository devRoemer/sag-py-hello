import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt", "r") as fin:
    REQS = fin.read().splitlines()

with open("requirements-dev.txt", "r") as fin:
    REQS_DEV = [item for item in fin.read().splitlines() if not item.endswith(".txt")]

setuptools.setup(
    name="sag-py-hello",
    version="0.1.0",
    description="A library to say hello.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/SamhammerAG/sag_py_hello",
    author="Samhammer AG",
    author_email="support@samhammer.de",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development",
    ],
    keywords="keyword, keyword",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"sag_py_hello": ["py.typed"]},
    python_requires=">=3.8",
    install_requires=REQS,
    extras_require={"dev": REQS_DEV},
    project_urls={
        "Documentation": "https://github.com/SamhammerAG/sag_py_hello",
        "Bug Reports": "https://github.com/SamhammerAG/sag_py_hello/issues",
        "Source": "https://github.com/SamhammerAG/sag_py_hello",
    },
)