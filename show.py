import streamlit as st
import pickle 
import numpy as np
from PIL import Image
import time
from win32com.client import Dispatch

extra=pickle.load(open('extra.pkl','rb'))



def predict_value(q,w,e,r,t,y,u,i):
    input=np.array([[q,w,e,r,t,y,u,i]])
    value=extra.predict(input)
    return float(value)

def main():

    st.title("---Diabetic Virtual Detector(DVD)---")
    st.write(" ")
    st.write(" ")
    im=Image.open("Fra.jpg")
    st.image(im,width=700)


    st.write("Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.Your body breaks down most of the food you eat into sugar (glucose) and releases it into your bloodstream. When your blood sugar goes up, it signals your pancreas to release insulin. Insulin acts like a key to let the blood sugar into your body’s cells for use as energy.")
    st.write(" ")
    st.write("With diabetes, your body doesn’t make enough insulin or can’t use it as well as it should. When there isn’t enough insulin or cells stop responding to insulin, too much blood sugar stays in your bloodstream. Over time, that can cause serious health problems, such as heart disease, vision loss, and kidney disease.")
    st.write(" ")
    st.write(" ")
    st.subheader(".......Check For diabetes at home!......\nJust fill out the parameters for ensuring the results with better accuracy ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")


    col1,col2=st.columns(2)
    with col1:
        a=st.number_input("Pregnancies(no.of times)")
    with col2:
        b=st.number_input("Glucose Level")
    c=st.number_input("BloodPressure(mm/hg)")
    d=st.number_input("SkinThickness(Tricep)")
    col1,col2=st.columns(2)
    with col1:
        e=st.number_input("Insulin Level")
    with col2:
        f=st.number_input("BMI(Body Mass Index)")
    g=st.number_input("DiabetesPedigreeFunction")
    h=st.number_input("Age")

    output=""
    btn=st.button("Predict")
    if btn:
        output=predict_value(a,b,c,d,e,f,g,h)
        awaaz = Dispatch("sapi.SpVoice")

        st.warning("Fetching your parameters Information...................")
        awaaz.Speak("Fetching your parameters Information")
        time.sleep(1)
        if output>0.5:
            st.error("Diabetic Report is Positive")
            awaaz.Speak("Sorry to say but Diabetic Report is Positive")
            
            st.subheader("But Don't worry,Eat Healthy Stay Healthy ")
            awaaz.Speak("Eat Healthy Stay Healthy")
            last=Image.open("R.jpg")
            st.image(last,width=790)
            
        
        else:
           
            st.success("Diabetic Report is Negative :) ")
            awaaz.Speak("Congratulations,You're absolutely fine ")
            
            last=Image.open("happ.jpg")
            st.image(last,width=590)


if __name__=='__main__':
    main()
    




