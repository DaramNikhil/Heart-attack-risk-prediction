import pickle
import os
import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score, accuracy_score
import pandas as pd


def object_saving(file, file_path: str):

    try:
        """_summary_

        Args:
            file_path (str): pickle file was stored in this location
            file (pickle): it returns the pickle file
        """

        with open(file_path, "wb") as f:

            pickle.dump(file, f)

    except Exception as e:
        logging.info("Failed to save objects: {}".format(e))


def train_algorithm(train_df, train_df_target, test_df, test_df_target, algorithms_, parameters):
    """finf the best algorithm
    """
    try:

        my_value = {}

        for i in range(len(list(algorithms_))):

            algorithms = list(algorithms_.values())[i]

            params = parameters[list(algorithms_.keys())[i]]

            gs = GridSearchCV(algorithms, params, cv=3)

            gs.fit(train_df, train_df_target)

            algorithms.set_params(**gs.best_params_)

            algorithms.fit(train_df, train_df_target)

            y_train_pred = algorithms.predict(train_df)

            y_test_pred = algorithms.predict(test_df)

            train_model_score = r2_score(train_df_target, y_train_pred)

            test_model_score = r2_score(test_df_target, y_test_pred)

            my_value[list(algorithms_.keys())[i]] = test_model_score

        final_algorithm = max(list(my_value))
        return final_algorithm
    

 

    except Exception as e:
        logging.error("Failed to train algorithm: {}".format(e))
        raise e
    
def file_read(file_path, df):
        with open(file_path, 'rb') as f:
            pcl = pickle.load(f)
            transformed_data = pcl.transform(df)
            return transformed_data
        
def model_func(model_path, df2):
    with open(model_path, 'rb') as model:
            model = pickle.load(model)
            pred = model.predict(df2)
            return pred







        





