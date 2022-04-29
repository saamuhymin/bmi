import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("Your Personal Body Mass Index (BMI) Instructor")

readme = st.checkbox("What is BMI?")

if readme:

    st.write("""
        Body mass index. A measure that relates body weight to height. BMI is sometimes used to measure total body fat and whether a person is a healthy weight. Excess body fat is linked to an increased risk of some diseases including heart disease and some cancers.
        According to <a href='https://en.wikipedia.org/wiki/Body_mass_index/'>Wikipedia </a>, Body mass index is a value derived from the mass and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms and height in metres.
        """, unsafe_allow_html=True)

    ###if(st.button("About")):
    ###st.text("Welcome To GeeksForGeeks!!!")
    
    
input_height = st.number_input("Write your height in centimeters (cm): ")
input_weight = st.number_input("Write your weight in kilograms (kg): ")

input_height = float(input_height)
input_weight = float(input_weight)

height = input_height
weight = input_weight

print("Your height is %f while your weight is %f", height, weight)

BMI = print(height / weight * weight)
print(BMI)

if BMI <= 18.5:
    print("You are underweight.")
    
elif BMI > 18.5 and BMI <= 24.9:
    print("You have a stable & normal weight.")
          
elif BMI > 24.9 and BMI <= 29.9:
     print("You are overweight.")
          
else:
     print("You are obese.")
          
      
          
          
  
    
    
   
