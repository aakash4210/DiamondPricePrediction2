import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

#below code is to create pkl file 
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path) #take that path name

        os.makedirs(dir_path, exist_ok=True) #and create that path

        with open(file_path, "wb") as file_obj:    #and crete pkl fil ein that path
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
###############################################################################
#tranining_pipline --> model_traininer---> used evaluate_model
#we take all ip data & list of models which w enned to check & retuen there report jaha he fun call hua he vaha(model_traininer ke code me)
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):  #take all model one by one 
            model = list(models.values())[i]

            # Train model
            model.fit(X_train,y_train)

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            #invert into report like (model = accu%)
            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
    

###############################################################################
#predict pipline --> load_object method , that we define here 
def load_object(file_path):
	try:
		with open(file_path, 'rb') as file_obj:
			return pickle.load(file_obj)
	except Exception as e:
		logging.info('Exception Occured in load_object functions utils')
		raise CustomException(e,sys)

