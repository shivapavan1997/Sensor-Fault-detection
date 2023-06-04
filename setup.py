from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns list of requirements
    """
    requirement_list:List[str]=[]

    """
    Write code to read to read requirements .txt file 
    and append in requirements_list
    """



    return requirement_list

setup(
name="sensor",
version="0.0.1",
author="shiva pavan",
author_email="sshivapavan1060@gmail.com",
packages=find_packages(),
install_requires=[],
)