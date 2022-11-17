from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# edit below variables as per your requirements -
# REPO_NAME = "REPO_NAME"
# AUTHOR_USER_NAME = ""
# SRC_REPO = "src"
# LIST_OF_REQUIREMENTS = []


setup(
    name='src',
    version="0.0.1",
    author="paragyech",
    description="A small package for DVC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{paragtech}/{dvc_project}",
    author_email="paragjain.tech@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
