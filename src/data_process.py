import pandas as pd
import numpy as np 
import logging

from src.data_ingestion import process_post
from src.data_evaluation import Data_Evaluation_fig
from src.data_clean import initialisation_config

def data_processing(data_path: str) ->pd.DataFrame:

    """data path passes from the data_processing

    Args:
        data_path (pd.DataFrame): data_path 
        
    """
    try:   
        train_data, test_data  = process_post(data_path)
        print("data splitted done....")
        train_arr, test_arr = initialisation_config().data_transformation(train_data,test_data)
        print("train_arr test_arr getting done....")
        best_model_score = Data_Evaluation_fig(train_arr, test_arr).data_clean()
        print("finded the best model score.....")
        print("best model score:", best_model_score)
        
        
               
    except Exception as e:
        logging.error("error occuring while evaluating data: {}". format(e))
        raise e

