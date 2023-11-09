# Will be responsible in making ML model a package and can even deploy in PyPi
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
# Function that will get all packages
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirments:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# Metadata of entire project
setup(
name='mlproject',
version='0.0.1',
author='Raghuram',
author_email='raghu.palani01@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)