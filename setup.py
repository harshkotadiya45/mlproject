from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str] :
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)
    return requirments

setup(
    name="mlproject",
    version="0.0.1",
    author="Harsh",
    author_email="23dcs051@charusat.edu.in",
    packages=find_packages(),
    install_requirements = get_requirements("requirements.txt")
)
