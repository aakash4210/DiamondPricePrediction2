
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    #trigger -->DataIngestion code
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    logging.info("complted DataIngestion & came back in piplines")
    print(train_data_path,test_data_path)
    logging.info("DataIngestion - code completed and return")
    
    #trigger -->DataTransformation code
    data_transformation =  DataTransformation()
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)
    #trigger -->ModelTrainer code
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)