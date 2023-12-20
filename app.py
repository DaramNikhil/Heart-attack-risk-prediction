import numpy as np
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template
import pandas as pd
from save_objects import file_read, model_func

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template('pred_page.html')        
    else:
        """data collection and transformation
        """
        Age = request.form.get("age")
        Sex = request.form.get("sex")
        Cholesterol = request.form.get("cholesterol")
        Heart_Rate = request.form.get("heartrate")
        Diabetes = request.form.get("diabetes")
        Family_History = request.form.get("family_history")
        Smoking = request.form.get("smoking")
        Obesity = request.form.get("obesity")
        Alcohol_Consumption = request.form.get("alchohol")
        Exercise_Hours_Per_Week = request.form.get("exercisehoursperweek")
        Previous_Heart_Problems = request.form.get("heart_problem")
        Medication_Use = request.form.get("medicationuse")
        Stress_Level = request.form.get("stresslevel")
        Sedentary_Hours_Per_Day = request.form.get("sadentory")
        BMI = request.form.get("bmi")
        Triglycerides = request.form.get("triglycerides")
        Physical_Activity_Days_Per_Week = request.form.get("pactivity")
        Sleep_Hours_Per_Day = request.form.get("sleep")
        Systolic_Blood_Pressure = request.form.get("systolic")
        Diastolic_Blood_Pressure = request.form.get("diastolic")
        

        my_dict = {"Age":Age,
                   "Sex":Sex,
                   "Cholesterol":Cholesterol,
                   "Heart Rate":Heart_Rate,
                   "Diabetes":Diabetes,
                   "Family History":Family_History,
                   "Smoking":Smoking,
                   "Obesity":Obesity,
                   "Alcohol Consumption":Alcohol_Consumption,
                   "Exercise Hours Per Week":Exercise_Hours_Per_Week,
                   "Previous Heart Problems":Previous_Heart_Problems,
                   "Medication Use":Medication_Use,
                   "Stress Level":Stress_Level,
                   "Sedentary Hours Per Day":Sedentary_Hours_Per_Day,
                   "BMI":BMI,
                   "Triglycerides":Triglycerides,
                   "Physical Activity Days Per Week":Physical_Activity_Days_Per_Week,
                   "Sleep Hours Per Day":Sleep_Hours_Per_Day
                   }
        df = pd.DataFrame(my_dict, index=[0])

        file_path = r"artifacts/transformer.pkl"

        model_path = r"artifacts/pred_obj.pkl"

        df2 = file_read(file_path, df)
        
        predictions = model_func(model_path, df2)

        return render_template('pred_page.html',predictions=predictions[0])
        
        
        

if __name__ == '__main__':
    app.run(debug=True)
