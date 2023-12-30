
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    #log file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)		#in current dir it create logs folder and put this log in it 
os.makedirs(logs_path,exist_ok=True)  #to create the folder , exist_ok = if alrady hoga to usme log file daldo 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #create log file path

logging.basicConfig(   			#for log we nned to define some things
	filename=LOG_FILE_PATH,    # filename 
	format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",   #what are the ling u want to log in file 
	level=logging.INFO     #
)