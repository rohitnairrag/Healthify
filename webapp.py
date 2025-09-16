import streamlit as st
import google.generativeai as genai
import os
import pandas as pd

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-2.5-flash-lite')


st.title('HEALTHIFY:green[ your personal AI health assistant]')
st.markdown('This application will assist you to have a better and healthy life.You can ask your health related questions and get personalized guidance')
tips='''Follow the steps
* Enter your details in the sidebar
* Enter your gender,age,height(cm),weight(Kgs)
* Select the number on the fitness scale(0-5).Where 5 means fittest and 0 means no fitness
* After filling the details  write your promt here and get customised response'''
st.write(tips)
st.sidebar.header(':green[ENTER YOUR DETAILS]')
name=st.sidebar.text_input('Enter your name')
gender=st.sidebar.selectbox('Select your gender',['Male','Female'])
age=st.sidebar.text_input('Enter your age')
weight=st.sidebar.text_input('Enter your weight in kgs')
height=st.sidebar.text_input('Enter your height in cm')

weight = pd.to_numeric(weight)
height = pd.to_numeric(height)
height_mts = height/100
bmi = weight/(height_mts**2)

fittness=st.sidebar.slider('Rate your fitness on a scale between 0 to 5',0,5,step=1)

st.sidebar.write(f'{name},Your BMI is {round(bmi,2)} kg/m^2')

#lets use genai model to get the output

user_query=st.text_input('Enter your question here')
promt=f'''Assume you are a health expert .You are required to answer the question asked by the user
.Use the details provided by the user.
name is {name}
gender is {gender}
age is {age}
weight is {weight} kgs
height is {height} cms
bmi is {bmi} kg/m^2
and user rates his/her fitness as {fittness} out of 5

Your output should be in bullet points
* It should start by giving one two line comment on the details that have been given
* It should explain what the real problem is based on the query asked by the user
* what could be the possible reason for the problem 
* What are the possible solutions
* you can also mention what doctor to see(specialization) if required
* strictly do not recommend any medice even if asked , just pass the message "Please reach out to your Doctor for Medication."
* output should be in bullet points and use tables whenever required
* use emojis to convey the emotions.

here is the query from the user {user_query}'''



if user_query:
    response=model.generate_content(promt)
    st.write(response.text)

