import streamlit as st
import requests
import joblib
import os
import streamlit as st
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize

def prediksi():
    data_actor = pd.read_csv('actor rank.csv', sep='\t')

    data_actor['actor'] = data_actor['actor'].str.lower()
    imdb_joblib = joblib.load('imdb_joblib')

    with st.form("Prediction Form"): 
        st.subheader('Worldwide Gross Prediction')
        st.write('\n')
        st.write('\n')
        st.write('Please specify the variable :')
        act1, act2, act3, act4 = st.columns(4)
        with act1:
            a1 = st.text_input('Input 1st Actor :')
        with act2:
            a2 = st.text_input('Input 2nd Actor :')
        with act3:
            a3 = st.text_input('Input 3rd Actor :')
        with act4:
            a4 = st.text_input('Input 4th Actor :')

        a1_value = data_actor['rank_actor'].loc[data_actor['actor'].str.contains(a1)].to_list()
        if a1 == '':
            a1_value = 1
        elif a1_value:
            a1_value = 1001 - a1_value[0]
        else:
            a1_value = 1
        a2_value = data_actor['rank_actor'].loc[data_actor['actor'].str.contains(a2)].to_list()
        if a2 == '':
            a2_value = 1        
        elif a2_value:
            a2_value = 1001 - a2_value[0]
        else:
            a2_value = 1
        a3_value = data_actor['rank_actor'].loc[data_actor['actor'].str.contains(a3)].to_list()
        if a3 == '':
            a3_value = 1
        elif a3_value:
            a3_value = 1001 - a3_value[0]
        else:
            a3_value = 1
        a4_value = data_actor['rank_actor'].loc[data_actor['actor'].str.contains(a4)].to_list()
        if a4 == '':
            a4_value = 1       
        elif a4_value:
            a4_value = 1001 - a4_value[0]
        else:
            a4_value = 1
        total_value = a1_value + a2_value + a3_value + a4_value

        set1, set2, set3, set4, set5 = st.columns(5)
        with set1:
            violence = st.select_slider('Choose Violence:', ('None', 'Mild', 'Moderate','Severe'))
            if violence == 'Mild':
                violence = 1
            elif violence == 'Moderate':
                violence = 2
            elif violence == 'Severe':
                violence = 3
            else:
                violence = 0
        with set2:
            nudity = st.select_slider('Choose Nudity:', ('None', 'Mild', 'Moderate','Severe'))
            if nudity == 'Mild':
                nudity = 1
            elif nudity == 'Moderate':
                nudity = 2
            elif nudity == 'Severe':
                nudity = 3
            else:
                nudity = 0
        with set3:
            profanity = st.select_slider('Choose Profanity:', ('None', 'Mild', 'Moderate','Severe'))
            if profanity == 'Mild':
                profanity = 1
            elif profanity == 'Moderate':
                profanity = 2
            elif profanity == 'Severe':
                profanity = 3
            else:
                profanity = 0
        with set4:
            alcohol = st.select_slider('Choose Alcohol:', ('None', 'Mild', 'Moderate','Severe'))
            if alcohol == 'Mild':
                alcohol = 1
            elif alcohol == 'Moderate':
                alcohol = 2
            elif alcohol == 'Severe':
                alcohol = 3
            else:
                alcohol = 0
        with set5:
            frightening = st.select_slider('Choose Frightening:', ('None', 'Mild', 'Moderate','Severe'))
            if frightening == 'Mild':
                frightening = 1
            elif frightening == 'Moderate':
                frightening = 2
            elif frightening == 'Severe':
                frightening = 3
            else:
                frightening = 0

        dur, bud = st.columns(2)
        with dur:
            duration = st.number_input('Movie Duration (in minutes):', min_value=30, max_value=300, value=120)
            duration = pd.to_numeric(duration)
        with bud:
            budget = st.number_input('Movie Budget (in USD million):', min_value = 1, max_value=500, value=200)
            budget = int(budget)*1000000

        data_predict = {'duration':duration, 'nudity':nudity, 'violence':violence, 'profanity':profanity,
                    'alcohol':alcohol, 'frightening':frightening, 'budget':budget, 'is_Action':1,
                    'is_Adventure':0, 'is_Comedy':1, 'is_Drama':0,
                    'is_Romance':1, 'is_Other':0,
                    'total_star_score':total_value
                    }

        data_predict= pd.DataFrame(data_predict, index=[0])
        poly_reg = PolynomialFeatures(degree = 2)
        data_predict = poly_reg.fit_transform(data_predict)

        submitted = st.form_submit_button("Predict")
        if submitted:
            res1, res2, res3 = st.columns(3)
            with res1:
                predict = imdb_joblib.predict(data_predict)
                predict = int(predict[0])
                predict = '$ ' + numerize.numerize(predict)
                st.write('**Worldwide Gross Prediction :**')
                st.info(predict)