import pandas as pd
import logging
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def clean_data(df: str)-> pd.DataFrame:
    """data cleaning and transformation

    Args:
        df (str): data preprocessing and data transformation

    Returns:
        pd.DataFrame: pd.DataFrame
    """
    

    """Pipelines
    """

           # numaric pipelines
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

                ]
            )

            # numaric values
    numaeics = [

                "Age"
            ]

    catagorics = [
                "Fever",
                "Cough",
                "Fatigue",
                "Difficulty Breathing",
                "Gender",
                "Blood Pressure",
                "Cholesterol Level",
            ]

    transformer = ColumnTransformer([

                ("numarics", numaric_pipelines, numaeics),

                ("catagoricals", catagorical_pipelines, catagorics)
            ])
    
    
    