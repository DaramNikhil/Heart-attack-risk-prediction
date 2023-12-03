import pandas as pd
import numpy as np

"""Data configuration class """
class Configuration:
    pass
class Init_configuration:
    def __init__(self, data_path):
        self.data_path = data_path

        """data initiated from the above path
        """
    def config_path(self)->None:
        return pd.read_csv(self.data_path)


#data passes from this function
def process_post(data_path):
    config_obj = Init_configuration(data_path)
    df = config_obj.config_path()
    return df
