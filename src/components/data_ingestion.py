import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

## intitialize the Data Ingestion configuration

@dataclass
class DataIngestionconfig:         #jo bhi data hame read karege banyage usko local me save kaha karege (do define karrahe )so again agin we no nned to do that work
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create the data ingestion class

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()     #here it will get all above paramters(train_data_path,test_data_path,raw_data_path)

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))  #we reaad data df
            logging.info('Dataset read as pandas Dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) #we make dir (artifict / under that creatd file -> raw.csv) #exist_ok : pehelese hoga to useme raw.csv banv , nihi hoda to new banv
            df.to_csv(self.ingestion_config.raw_data_path,index=False) #we save that df --> raw.csv
            logging.info('Raw data is created')
            #2nd operstion :- split the data into train & test data set & save inito a files
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)  #code to perfeom split
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #train_set --> data save karo train.csv me
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)   #test_set --> data save karo test.csv me
            logging.info('Ingestion of Data is completed')
            #after succesfully completed both the operations  we retuen there paths 
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) 
        except Exception as e:#if any error in try block this will handle it
            logging.info('Exception occured at Data Ingestion Stage')
            raise CustomException(e,sys)
