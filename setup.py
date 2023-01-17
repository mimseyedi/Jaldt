import setuptools

with open("README.md", "r", encoding = "utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name = "jaldt",
    version = "1.0.0",
    author = "mimseyedi",
    author_email = "mim.seyedi@gmail.com",
    description = "Jaldt is a package for working with date and time based on Jalali calendar and date.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mimseyedi/Jaldt",
    packages = setuptools.find_packages(where="src"),
    package_dir = {"": "src"},
    python_requires = ">=3.6",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)