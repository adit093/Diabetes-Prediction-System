import streamlit as st
import pickle
import numpy as np

# Load saved model
loaded_model = pickle.load(open('Trained_model.sav', 'rb'))

# App title
st.title('Diabetes Prediction System')

st.write('Enter patient details below:')

# Input fields
pregnancies = st.number_input('Number of Pregnancies', min_value=0)
glucose = st.number_input('Glucose Level', min_value=0)
blood_pressure = st.number_input('Blood Pressure', min_value=0)
skin_thickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin Level', min_value=0)
bmi = st.number_input('BMI', min_value=0.0)
diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0)
age = st.number_input('Age', min_value=1)

# Prediction button
if st.button('Predict'):

    input_data = np.array([
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree,
        age
    ]).reshape(1, -1)

    prediction = loaded_model.predict(input_data)

    if prediction[0] == 0:
        st.success('The person is NOT diabetic')
    else:
        st.error('The person is diabetic')