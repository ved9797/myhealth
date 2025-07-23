from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import pandas as pd
import google.generativeai as genai

# Configure the key
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# ----------- SIDEBAR: BMI Calculator -------------
st.sidebar.title("BMI Calculator ✍️")

# User inputs in sidebar
weight = st.sidebar.number_input("Weight (in kgs):", min_value=1)
height = st.sidebar.number_input("Height (in cms):", min_value=1)

# Calculate BMI
if weight > 0 and height > 0:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.sidebar.write("**The BMI is:**", round(bmi, 2))

    # Show category
    st.sidebar.markdown("### The BMI value can be interpreted as:")
    if bmi < 18.5:
        st.sidebar.warning("Underweight - PLEASE EAT")
    elif 18.5 <= bmi <= 24.9:
        st.sidebar.success("Normal Weight-ACHA HAI")
    elif 25 <= bmi <= 29.9:
        st.sidebar.info("Overweight-KAMM KHAA YAAR")
    else:
        st.sidebar.error("Obese- BASS SAANS LE YAAR")

# BMI Range Legend (Always visible)
st.sidebar.markdown("""
---  
**BMI Categories:**  
- Underweight: BMI < 18.5  
- Normal Weight: BMI 18.5 - 24.9  
- Overweight: BMI 25 - 29.9  
- Obese: BMI > 30  
""")

# ----------- MAIN AREA: Healthcare Advisor -------------
st.title("👨‍⚕️ Healthcare Advisor 🩺")

# Chat input
input = st.text_input("Hi! I am your medical expert 💊. Ask me information about Health, Diseases & Fitness Only")



# Disclaimer section
st.markdown("---")
st.subheader("Disclaimer:")
st.write("1. This is an AI Advisor and should not be construed as Medical Advice.")
st.write("2. Before taking any action, it is recommended to consult a Medical Practitioner.")

def guide_me_on(input):
    model = genai.GenerativeModel("gemini-2.5-pro")
    if input!="":
        prompt = f''' Act as a Dietician, Health coach and Expert and address the queries, questions, apprehensions 
        related to health,fitness, diseases and things associated with empathy towards the user. Any query or
        question that is not related to health should pass the following message - "I am a Healthcare Expert and 
        I can answer questions related to Health, Fitness and Diet only."
        If someone asks about medicine for any ailment, just pass the message - "I am an AI model and cannot 
        answer questions related to diagnosis and medicines. Please reach out to your doctor"
        Note: Use Emojis, to givea personal touch '''
        
        response = model.generate_content(prompt+input)
        return(response.text)
    else:
        return(st.write("Please write the Prompt"))
    
# submit button
submit = st.button("Submit")
if submit:
    response = guide_me_on(input)
    st.subheader(":blue[response]")
    st.write(response)