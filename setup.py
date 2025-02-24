from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "Priyanka"
SRC_REPO = "src"
AUTHOR_EMAIL = "abc@gmail.com"

setup(
    name=SRC_REPO,
    version="0.0.0",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Deep Learning CNN based model",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"": "src"},
    packages=find_packages(where="src")
)