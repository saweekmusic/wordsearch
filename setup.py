from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wordsearch-gen",  # ✅ Your PyPI package name
    version="0.1.0",
    author="Sviatoslav Trofymenko",
    author_email="sviatoslavtrofymenko@icloud.com",  # Replace with your email
    description="A customizable word search puzzle generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saweekmusic/wordsearch",  # Update if needed
    project_urls={
        "Bug Tracker": "https://github.com/saweekmusic/wordsearch/issues",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),  # Automatically finds 'wordsearch' package
    python_requires=">=3.7",
    include_package_data=True,
)
