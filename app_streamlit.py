import streamlit as st
import pickle
import pandas as pd
import numpy as np

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

def welcome_page():
    return "Welcome."


def PredictNoteAuthentication(variance,skewness,curtosis,entropy):       
       prediction = classifier.predict([[variance, skewness, curtosis, entropy]])        
       return prediction
      


def main():
    st.title("Bank Note Authenticator")
    html_temp= """
       <div style="background-color:tomato;padding:10px>
       <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator</h2>
       </div>
               """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input('variance','Type here')        
    skewness = st.text_input('skewness','Type here')        
    curtosis = st.text_input('curtosis','Type here')       
    entropy = st.text_input('entropy','Type here')
    result=""
    if st.button("Predict"):
        result=PredictNoteAuthentication(variance,skewness,curtosis,entropy)
        st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")   

if __name__=='__main__':
      main()