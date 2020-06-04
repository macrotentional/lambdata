from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-martin", # the name that you will install via pip
    version="1.12",
    author="Martin Campbell",
    author_email="macrotentional@gmail.com",
    description="setup for week 9 day 1 project",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/macrotentional/lambdata-martin",
    #keywords="",
    packages= ["my_lambdata"] #find_packages() # ["my_lambdata"]
)