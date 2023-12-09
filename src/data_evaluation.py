import pandas as pd
import numpy as np
from src.data_clean import clean_data
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


class Data_Evaluation_fig:
    def __init__(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data

    def data_clean(self):
        """Data transformation 
                and feature scaling

        Args:
            (df): transformed data
            
        """

        """merge the data"""
        data_merge = np.c_[self.train_data, np.array(self.test_data)]
        
        """splitting the data into training and testing
        """
        X = data_merge[:,:-1]
        y = data_merge[:,-1]
        # Split into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Apply SMOTE
        sm = SMOTE(random_state=42)
        X_res, y_res = sm.fit_resample(X_train, y_train)

        # Now, X_res and y_res are the resampled data
        
