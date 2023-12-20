import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
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
                    ("lec", OneHotEncoder(handle_unknown="ignore")),
                    ("scaler", StandardScaler(with_mean=False))

                ])

            # numaric values
            numarics = ['Age', 'Cholesterol', 'Heart Rate', 'Diabetes',
                     'Family History', 'Smoking', 'Obesity', 
                     'Alcohol Consumption', 'Exercise Hours Per Week',
                       'Previous Heart Problems', 'Medication Use',
                         'Stress Level', 'Sedentary Hours Per Day', 'BMI', 'Triglycerides', 
                         'Physical Activity Days Per Week','Sleep Hours Per Day']

            catagorics = ['Sex']


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
            train_data_input_feature = train_data.drop("Heart Attack Risk", axis=1)
            
            # test_data_targer_feature
            train_data_target_feature = train_data["Heart Attack Risk"].values
            
            # test_data_input_feature
            test_data_input_feature = test_data.drop("Heart Attack Risk", axis=1)

            # test_data_targer_feature
            test_data_target_feature = test_data["Heart Attack Risk"].values

            train_arr_file = transformer.fit_transform(
                train_data_input_feature)

            """save the scaling object in the form of pickle file
            """

            """make a directory for storage purpose

            """
            os.makedirs(os.path.dirname(self.data_process_config.data_path), exist_ok= True)

            object_saving(transformer, self.data_process_config.data_path)

            test_arr_file = transformer.transform(test_data_input_feature)

            train_arr_transform = np.c_[train_arr_file, np.array(train_data_target_feature)]
        
            test_arr_transform = np.c_[test_arr_file, np.array(test_data_target_feature)]


            
            return (

                train_arr_transform,
                test_arr_transform,
            )

        except Exception as e:
            raise e