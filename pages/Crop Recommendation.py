import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings
import base64



def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Crop Recommendation Engine 🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.subheader("Let AI help you in finding your suitable crop.")
   
    
    N = st.number_input("Nitrogen", 1,10000)
    P = st.number_input("Phosphorus", 1,10000)
    K = st.number_input("Potassium", 1,10000)
    temp = st.number_input("Temperature",0.0,100000.0)
    humidity = st.number_input("Humidity in %", 0.0,100000.0)
    ph = st.number_input("Ph", 0.0,100000.0)
    rainfall = st.number_input("Rainfall in mm",0.0,100000.0)

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1,-1)
    print(single_pred)
    if st.button('Predict'):

            loaded_model = load_model('crop_modelSVC.pkl')
            prediction = loaded_model.predict(single_pred)
            st.write('''
		    ## Results 🔍 
		    ''')
            
            a = prediction.item()
            
            crops = ['apple', 'banana', 'blackgram', 'chickpea', 'coconut', 'coffee', 'cotton', 'grapes', 'jute', 'kidneybeans', 'lentil', 'maize', 'mango', 'mothbeans', 'mungbean', 'muskmelon', 'orange', 'papaya', 'pigeonpeas', 'pomegranate', 'rice', 'watermelon']
            

            st.success(f"{crops[a]} is recommended by the A.I for your farm.")
            
      

    
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)



if __name__ == '__main__':
	main()

