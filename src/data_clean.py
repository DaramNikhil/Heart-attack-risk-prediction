import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import os
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from save_objects import object_saving

class data_process_config:

    data_path = os.path.join(r"D:\my projects\heart_attack_risk_prediction\heart_attack_risk_prediction\artifacts", "transformer.pkl")




class initialisation_config:

    def __init__(self) -> None:

        self.data_process_config = data_process_config()

    def data_transformation(self, train_data, test_data):

        try:

            # pipelines

           # numaric pipelines
            numaric_pipelines = Pipeline(

                [
                    ("scaler", StandardScaler())

                ]
            )

            # catagorical pipelies
            catagorical_pipelines = Pipeline(

                [
                    ("ohe", OneHotEncoder(handle_unknown="error")),
                    ("scaler", StandardScaler(with_mean=False))

                ])

            # numaric values
            numarics = ['Age', 'Cholesterol', 'Heart Rate', 'Diabetes',
                     'Family History', 'Smoking', 'Obesity', 
                     'Alcohol Consumption', 'Exercise Hours Per Week',
                       'Previous Heart Problems', 'Medication Use',
                         'Stress Level', 'Sedentary Hours Per Day', 'BMI', 'Triglycerides', 
                         'Physical Activity Days Per Week', 
                         'Sleep Hours Per Day']

            catagorics = ['Sex', 'Diet']


            transformer = ColumnTransformer(
            transformers=[

                ("numaricals", numaric_pipelines, numarics),

                ("catagoricals", catagorical_pipelines, catagorics)
            ], remainder="passthrough")

             # test_data
            """
            splitting the data into training and testing sets for training 
            """
            # train_data_input_feature
            train_data_input_feature = train_data.iloc[:, :-1]

            # test_data_targer_feature
            train_data_target_feature = train_data.iloc[:, -1]

            # test_data_input_feature
            test_data_input_feature = test_data.iloc[:, :-1]

            # test_data_targer_feature
            test_data_target_feature = test_data.iloc[:, -1]

            train_arr_file = transformer.fit_transform(
                train_data_input_feature)

            """save the scaling object in the form of pickle file
            """

            """make a directory for storage purpose

            """
            os.makedirs(os.path.dirname(self.data_process_config.data_path), exist_ok= True)

            object_saving(transformer, self.data_process_config.data_path)

            test_arr_file = transformer.transform(test_data_input_feature)

            
            return (

                train_arr_file,
                test_arr_file,
            )

        except Exception as e:
            raise e