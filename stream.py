import streamlit as st
import pandas as pd
import pickle
import streamlit.components.v1 as components

#file_paths
scale_file_path = r"artifacts/transformer.pkl"
pred_file_path = r"artifacts/pred_obj.pkl"

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Load the trained model


st.title('“HeartShield ❤️: Predictive Heart Attack Risk Assessment”')
st.markdown("""
    “Leveraging advanced algorithms for early detection of heart attack risks. Stay informed, stay healthy.”
""")

# Input features
with st.container():

    Name = st.text_input('Enter your name')
    age = st.slider('How old are you?', 0, 90, 18)
    st.write("I'm ", age, 'years old')
    gender = st.selectbox('Gender', ['Male', 'Female'])
    cholesterol = st.number_input('Cholesterol level', min_value=100, max_value=400, value=200)
    heart_rate = st.number_input('Mension your heart rate', min_value=40, max_value=130, value=72)
    heart_disease_fm = st.selectbox('Any heart diseases in your family?', ['Yes', 'No'])
    smoking = st.selectbox('Do you have smoking habbit?', ['Yes', 'No'])
    obesity = st.selectbox('Obesity', ['Yes', 'No'])
    alchohol = st.selectbox('Do you take alchohol?', ['Yes', 'No'])
    diabetes = st.selectbox('Do you have dabetes?', ['Yes', 'No'])
    excersice_hours_per_week = st.slider('Execersice hours per week?', 0, 5, 19)
    st.write("I'm doing ", excersice_hours_per_week, 'hours per week')
    Previous_Heart_Problems = st.selectbox('Previous heart problem?', ['Yes', 'No'])
    medicationuse  = st.selectbox('Medication use', ['Yes', 'No'])
    stresslevel = st.number_input('Stress level', min_value=0, max_value=10)
    Sedentary = st.number_input('Sedentary hours per day', min_value=0, max_value=12)
    bmi = st.number_input('BMI', min_value=0, max_value=40)
    triglycerides = st.number_input('Triglycerides', min_value=1, max_value=400)
    Physical_Activity_Days_Per_Week = st.number_input('physical activity per week', min_value=0, max_value=9)
    sleep_per_day = st.number_input('Sleep hours per day', min_value=0, max_value=10)


    with st.container():
        my_data = my_dict = {"Age":age,
                   "Sex": gender,
                   "Cholesterol":cholesterol,
                   "Heart Rate":heart_rate,
                   "Diabetes":diabetes,
                   "Family History":heart_disease_fm,
                   "Smoking":smoking,
                   "Obesity":obesity,
                   "Alcohol Consumption":alchohol,
                   "Exercise Hours Per Week":excersice_hours_per_week,
                   "Previous Heart Problems":Previous_Heart_Problems,
                   "Medication Use":medicationuse,
                   "Stress Level":stresslevel,
                   "Sedentary Hours Per Day":Sedentary,
                   "BMI":int(bmi),
                   "Triglycerides":triglycerides,
                   "Physical Activity Days Per Week":Physical_Activity_Days_Per_Week,
                   "Sleep Hours Per Day":sleep_per_day
                   }

        df = pd.DataFrame(my_data, index=[0])

        df["Diabetes"] = [1 if i == "Yes" else 0 for i in df.Diabetes]
        df["Family History"] = [1 if i == "Yes" else 0 for i in df["Family History"]]
        df["Smoking"] = [1 if i == "Yes" else 0 for i in df.Smoking]
        df["Obesity"] = [1 if i == "Yes" else 0 for i in df.Obesity]
        df["Alcohol Consumption"] = [1 if i == "Yes" else 0 for i in df["Alcohol Consumption"]]
        df["Previous Heart Problems"] = [1 if i == "Yes" else 0 for i in df["Previous Heart Problems"]]
        df["Medication Use"] = [1 if i == 1 else 0 for i in df["Medication Use"]]

        def file_read(file_path, df):
            with open(file_path, 'rb') as f:
                pcl = pickle.load(f)
                transformed_data = pcl.transform(df)
                return transformed_data
        
        def model_func(model_path):
            with open(model_path, 'rb') as model:
                    model = pickle.load(model)
                    return model
            
    
        transform = file_read(scale_file_path, df)
        model = model_func(pred_file_path)

        predictions = model.predict(transform)

        with st.container():
         
            if st.button("Predict", key="heart", help="A stylish button"):
                if predictions == 1:
                    st.warning('Elevated Heart Attack Risk Detected', icon="⚠️")
                    st.warning("Our system has identified a potential high risk of heart attack based on your inputs. This is a serious health concern and immediate medical attention is strongly advised. Please remember, this app is not a replacement for professional medical advice. Always consult with a healthcare professional for accurate information.", icon="⚠️"
                    )
                else:
                    st.success("Good News: Low Heart Attack Risk Detected")
                    st.success("Our analysis indicates a low risk of heart attack based on your inputs. This is a positive sign for your heart health. However, continue to maintain a healthy lifestyle and regular check-ups with your healthcare provider. Remember, this app is intended for informational purposes only and is not a substitute for professional medical advice.", icon="✅")


                with st.container():
                    st.markdown("#####")
                    st.markdown("####")
                    st.markdown("##### Thanks for visiting!  \nCreated with ❤ by {}".format(Name))





