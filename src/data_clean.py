import pandas as pd
import logging
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import os
from save_objects import object_saving

class Configuration:
    """file location
    """
    data_path = os.path.join(r"D:\my projects\heart_attack_risk_prediction\heart_attack_risk_prediction\artifacts", "transformer.pkl")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    """preprocessing the data using simple imputer"""
    try:

        """remove some
        unimportent features from the datarame"""

        df = df.drop(["Income","Patient ID","Country","Continent","Hemisphere"], axis=1)


        """extracting columns from the dataset"""

        #numaric columns
        numarics = ['Age', 'Cholesterol', 'Heart Rate', 'Diabetes',
                     'Family History', 'Smoking', 'Obesity', 
                     'Alcohol Consumption', 'Exercise Hours Per Week',
                       'Previous Heart Problems', 'Medication Use',
                         'Stress Level', 'Sedentary Hours Per Day', 'BMI', 'Triglycerides', 
                         'Physical Activity Days Per Week', 
                         'Sleep Hours Per Day']
        
        #catagorical columns
        catagorics = ['Sex', 'Blood Pressure', 'Diet']

        #numarical pipeline
        numaric_pipelines = Pipeline(

                [
                    ("scaler", StandardScaler())

                ]
            )

            # catagorical pipelies
        catagorical_pipelines = Pipeline(

                [
                    ("ohe", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))

                ])

        transformer = ColumnTransformer([

                ("numaricals", numaric_pipelines, numarics),

                ("catagoricals", catagorical_pipelines, catagorics)
            ])
        
        """splpit the data into 
                training and testig"""
        train_data = df.iloc[:,:-1]
        test_data = df.iloc[:,-1]

        """applying the column transformation"""

        transformed_data = transformer.fit_transform(train_data).toarray()

        """created a folders to save
                artifacts
        """
        path_obj = Configuration()
        os.makedirs(os.path.dirname(path_obj.data_path), exist_ok=True)

        """save the object in pickle file"""
          
        object_saving(
            transformer, 
            path_obj.data_path)

        return (
            transformed_data,
            test_data
        )
    

    except Exception as e:
        logging.error("error occuring while running clean data function: {}".format(e))
        raise e
    


        