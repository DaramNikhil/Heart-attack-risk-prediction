import pandas as pd
import numpy as np
import logging
from sklearn.model_selection import train_test_split

"""Data configuration class """
class Configuration:
    pass
class Init_configuration:
    def __init__(self, data_path):
        self.data_path = data_path

        """data initiated from the above path
        """
    def config_path(self)->None:
        try:

            df = pd.read_csv(self.data_path)
            """remove some
                unimportent features from the datarame"""

            df = df.drop(["Income","Patient ID","Country","Continent","Hemisphere","Blood Pressure"], axis=1)
            return df

        except Exception as e:
            logging.error("Configuration error : {}".format(e))
            raise e


#data passes from this function
def process_post(data_path):

    config_obj = Init_configuration(data_path)
    df = config_obj.config_path()
    train_data, test_data = train_test_split(df, test_size=0.2, random_state= 1)
    return (
        train_data,
        test_data
    )

