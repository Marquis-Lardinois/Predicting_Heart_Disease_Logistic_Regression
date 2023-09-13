from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function returns requirements list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove((HYPHEN_E_DOT))
setup(
    name='Predicting_Heart_Disease_Logistic_Regression',
    version='0.0.1',
    author='Marquis',
    author_email='Marquislard@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )