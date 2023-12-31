import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

#this below all model we created, we use them in this code 
from src.components.data_ingestion import DataIngestion


if __name__=='__main__':            #from this code we want to triiger DataIngestion code so we use that
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    