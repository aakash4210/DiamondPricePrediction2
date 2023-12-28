from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

#insted of hared code the value we take requirements.txt file contain 
#we pass requirements.txt --> to get_requirements () , we take all lib name and put into requirements[] list
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:       #here we open requirements.txt file
        requirements=file_obj.readlines()   #here we read requirements.txt file contain line by line   #pandas \n numpy \n seaborn \n
        requirements=[req.replace("\n","") for req in requirements]  ##when we move to nect line (\n) will come to remove it we write this 

        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements                 #give all lib name only  :- pandas numpy seaborn 
        

setup(
    name='DiamondPriceprediction',
    version='0.0.1',
    author='Aakash',
    author_email="aspersonal22@gmail.com",
    install_requires=get_requirements('requirements.txt'),#this will directly read packages name from requirements.txt file 
    packages=find_packages()

)