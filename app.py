import streamlit as st


import numpy as np
import pandas as pd
import joblib


model = joblib.load('model.pkl')

st.title('Did they survive :ship:')

passengerid = st.text_input('Input Passenger Id', "123456")
passengerclass = st.select_slider('Choose Passenger Class',[1,2,3])
name = st.text_input('Input Passenger Name', "John Smith")
gender = st.select_slider('Select Gender',['Male','Female'])
age = st.slider('Input Age',0,100)
sibsp = st.slider('Input Siblings',0,10)
parch = st.slider('Input parents/children',0,2)
ticketid = st.number_input('Ticket Number',1234)
fare = st.number_input('Fare Amount, 0,100')
cabin = st.text_input('Enter Cabin', "C52")
embarked = st.selectbox('Choose embarkation point',["S","C","Q"])

gender = 1 if gender=='Male' else 0

companions = sibsp+parch+1
alone = 1 if companions==1 else 0
small = 1 if 2<=companions<=4 else 0
large = 1 if companions>4 else 0


pclass_1 = 1 if passengerclass==1 else 0
pclass_2 = 1 if passengerclass==2 else 0
pclass_3 = 1 if passengerclass==3 else 0

embarked_S = 1 if embarked=='S' else 0
embarked_C = 1 if embarked=='C' else 0
embarked_Q = 1 if embarked=='Q' else 0

# columns = ['PassengerId', 'Gender', 'Name', 'Sex', 'Age', 'SibSp', 'Parch','Ticket', 'Fare', 'Cabin', 'Embarked']

def predict():
    row = np.array([passengerid,gender,age,sibsp,parch,fare,companions,alone,small,large,pclass_1,pclass_2,pclass_3,embarked_S,embarked_C,embarked_Q])
    X = pd.DataFrame([row])

    print(X)
    prediction = model.predict(X)


    if prediction[0] == 1:
        st.success('Passenger Survived :thumbsup:')
    else:
        st.error('Passenger did not Survive :thumbsdown:')


st.button('Predict', on_click = predict)