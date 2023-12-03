import pandas as pd
import numpy as np 
import logging

from src.data_ingestion import process_post
from src.data_evaluation import Evaluate_data
from src.data_clean import clean_data


def data_processing(data_path: str) ->pd.DataFrame:
    """data path passes from the data_processing

    Args:
        data_path (pd.DataFrame): data_path 
        
    """
    try:   
        df = process_post(data_path) 
        clean_data(df)
        Evaluate_data(df)
        return df
    except Exception as e:
        logging.error("error occuring while evaluating data: {}". format(e))
        raise e

