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
        
        st.button('What should I do?')
            st.write("Don't be picky at whatever you eat. Simply just eat everything.")
            st.write("Just eat everything but don't be so dumb. You still have to include nutrient-rich foods. Bear that in mind.")
            st.write("Reduce drinking soda or sparkling water. Consume smoothies and shakes that contain calories and protein instead.")
            st.write("Add more toppings for more calories but don't take too much sugar and fat.")
            st.write("Do all of these above and remember to exercise to help you to gain weight by building up muscles."
        

    
    elif BMI > 18.5 and BMI <= 24.9:
        st.success("You have a stable & normal weight.")
        
        st.button('What should I do?')
            st.write("Just hang in there! Be consistent and dedicate to what you are doing now.")
                     
          
    elif BMI > 24.9 and BMI <= 29.9:
        st.warning("You are overweight.")
        
        st.button('What should I do?')
            st.write("A healthy diet. Basically, you should revise the food triangle chart. What should be eaten plenty, some and a few in terms of amount.")
            st.write("Exercise is a must. You gotta reduce and burn the foods you just ate.")
            st.write("Always check the calorie information to prevent daily excessive intake.")
          
    else:
        
        st.error("You are obese.")
        
        st.button('What should I do?')
            st.write("A healthy diet. Basically, you should revise the food triangle chart. What should be eaten plenty, some and a few in terms of amount.")
            st.write("Exercise is a must. You gotta reduce and burn the excessive fat.")
            st.write("Get a professional trainer and dietitian to guide you effectively.")
      
          
          
  
    
    
   
