import streamlit as st

import numpy as np
import pandas as pd
import time

st.header("Your Personal Body Mass Index (BMI) Advisor")

readme = st.checkbox("What is BMI?")

if readme:
    
    a_string = "right"
    width = 50
    readme = a_string.rjust(width)
    
    st.write("""
        Body mass index. A measure that relates body weight to height. BMI is sometimes used to measure total body fat and whether a person is a healthy weight. Excess body fat is linked to an increased risk of some diseases including heart disease and some cancers.
        According to <a href='https://en.wikipedia.org/wiki/Body_mass_index/'>Wikipedia</a>, Body mass index is a value derived from the mass and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms and height in metres.
        """, unsafe_allow_html=True)
    

        
    
input_height = st.number_input("Write your height in centimeters (cm): ")
input_weight = st.number_input("Write your weight in kilograms (kg): ")

input_height = int(input_height)
input_weight = float(input_weight)

if(st.button("Submit")):
    st.write(f"Your height is {input_height}cm")
    st.write(f"Your weight is {input_weight:.1f}kg")
    
    height = input_height
    weight = input_weight
    
    height = height/100
    BMI = (weight / height**2)
    st.write(f"Your BMI is {BMI:.2f}")

    if BMI <= 18.5:
        st.info("You are underweight.")
        result = ("Nice")
        
        if st.button("Click me?"):
            st.text(result)
      
        
    
    
