import numpy as np
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template


app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template('home_page.html')        
    else:
        """data collection and transformation
        """
        Age = request.form["age"]
        Sex = request.form["sex"]
        Cholesterol = request.form["cholesterol"]
        Heart_Rate = request.form["heartrate"]
        Diabetes = request.form["diabetes"]
        Family_History = request.form["family_history"]
        Smoking = request.form["smoking"]
        Obesity = request.form["obesity"]
        Alcohol_Consumption = request.form["alchohol"]
        Exercise_Hours_Per_Week = request.form["exercisehoursperweek"]
        Previous_Heart_Problems = request.form["heart_problem"]
        Diet = request.form["age"]
        Medication_Use = request.form["medicationuse"]
        Stress_Level = request.form["stresslevel"]
        Sedentary_Hours_Per_Day = request.form["sadentory"]
        BMI = request.form["bmi"]
        Triglycerides = request.form["triglycerides"]
        Physical_Activity_Days_Per_Week = request.form["pactivity"]
        Sleep_Hours_Per_Day = request.form["sleep"]

        my_dict = {}


        return render_template('pred_page.html')
        
        
        

if __name__ == '__main__':
    app.run(debug=True)
