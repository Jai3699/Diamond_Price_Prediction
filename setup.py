from setuptools import setup,find_packages
from typing import List

hyph_dot_e="-e ."

def get_requirements(file_path:str)->List[str]:  ## it will return list which contains names in string

    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if hyph_dot_e in requirements:
            requirements.remove(hyph_dot_e)
        return requirements
    
setup(
    name='Diamond_Price_Prediction',
    version='1.0',
    author='Jai',
    author_email='jaiyadav3699@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages() ##to find different submodules
)