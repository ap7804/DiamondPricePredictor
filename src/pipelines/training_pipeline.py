import os
import sys
from ..logger import logging  # This import should work now
from ..exception import CustomException
import pandas as pd
from ..components.data_ingestion import Dataingestion
from ..components.model_trainer import ModelTrainer
from ..components.data_transformation import DataTransformation
if __name__ == '__main__':
    obj = Dataingestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)

    data_transformation=DataTransformation()

    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
    
    model_trainer=ModelTrainer()
    
    model_trainer.initate_model_training(train_arr,test_arr)



