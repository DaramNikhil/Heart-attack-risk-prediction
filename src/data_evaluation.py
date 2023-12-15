import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from save_objects import train_algorithm, object_saving
import os
from sklearn.metrics import r2_score


class Data_Evaluation_fig:
    def __init__(self, train_arr, test_arr):

        self.train_arr = train_arr
        self.test_arr = test_arr
    

    def data_clean(self) -> None:

        try:

            """model traning and hyper parameter tuning
        """
            
            algorithms_ = {'RandomForestClassifier': RandomForestClassifier(),
                           "SVC": SVC(),
                           "GaussianNB": GaussianNB(),
                           "KNN": KNeighborsClassifier(n_neighbors=5),
                           "DecisionTreeClassifier": DecisionTreeClassifier(),

                           }

            """
            split the trainig and test data"""

            train_arr_input = self.train_arr[:, :-1]
            train_arr_target = self.train_arr[:, -1]
            test_arr_input = self.test_arr[:, :-1]
            test_arr_target = self.test_arr[:, -1]


            #data path location
            data_path = os.path.join(r"D:\my projects\heart_attack_risk_prediction\heart_attack_risk_prediction\artifacts", "pred_obj.pkl")

            os.makedirs(os.path.dirname(data_path), exist_ok=True)

            """
            hyper parameter tuning parameters"""
            parameters = {
                "RandomForestClassifier": {"max_depth": [2, 3, 5, 10, 20],
                                           "criterion": ["gini", "entropy"],
                                           "max_features": ["sqrt", "log2"],
                                           "min_samples_split": [2, 5, 10],
                                           "min_samples_leaf": [1, 2, 4]
                                           },

                "SVC": {"C": [0.1, 1, 10, 100, 1000],
                        "kernel": ["rbf", "linear"],
                        "gamma": [1, 0.1, 0.01, 0.001, 0.0001]
                        },

                "GaussianNB": {
                },


                "DecisionTreeClassifier": {"min_samples_split": [2, 5, 10],
                                           "min_samples_leaf": [1, 2, 4]
                                           },

                "KNN": {

                },

                
            }

            """
                apply the algorithm and gridsearch to the model and return the result as a dictionary"""

            best_algorithm = train_algorithm(

                train_arr_input,
                train_arr_target,
                test_arr_input,
                test_arr_target,
                algorithms_,
                parameters)

            main_algorithm = algorithms_[str(best_algorithm)]

            main_algorithm.fit(train_arr_input, train_arr_target)

            object_saving(main_algorithm,
                             data_path)

            prediction = main_algorithm.predict(test_arr_input)

            model_scores = r2_score(test_arr_target, prediction)

            return model_scores
            

        except Exception as e:
            logging.error("error occuring during in the data_clean process: {}".format(e))
            raise e
        
