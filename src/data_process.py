import pandas as pd
import numpy as np 
import logging

from src.data_ingestion import process_post
from src.data_evaluation import Data_Evaluation_fig
from src.data_clean import clean_data


def data_processing(data_path: str) ->pd.DataFrame:
    """data path passes from the data_processing

    Args:
        data_path (pd.DataFrame): data_path 
        
    """
    try:   
        df = process_post(data_path)
        transformed_data, test_data = clean_data(df=df)
        merge_data = Data_Evaluation_fig(transformed_data, test_data).data_clean()
        print(merge_data)
        
    except Exception as e:
        logging.error("error occuring while evaluating data: {}". format(e))
        raise e

