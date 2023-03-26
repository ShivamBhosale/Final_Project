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
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Fertilizer Recommendation Engine 🧪 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.subheader("Get the suitable Fertilizer for your Crops.")
   
    
    temp = st.number_input("Temperature", 1,10000)
    P = st.number_input("Humidity", 1,10000)
    K = st.number_input("Moisture", 1,10000)
    soilType = st.number_input("Soil Type",0.0,100000.0)
    humidity = st.number_input("Crop Type", 0.0,100000.0)
    Nitrogen = st.number_input("Nitrogen",0.0,100000.0)
    Potassium = st.number_input("Potassium",0.0,100000.0)
    K = st.number_input("Phosphorous",0.0,100000.0)
    

    feature_list = [temp, P, K, soilType, humidity,Nitrogen, Potassium,K]
    single_pred = np.array(feature_list).reshape(1,-1)
    print(single_pred)
    if st.button('Predict'):

            loaded_model = load_model('Fertlizer.pkl')
            prediction = loaded_model.predict(single_pred)
            st.write('''
		    ## Results 🔍 
		    ''')
            a = prediction.item()
            
            fertilizer_names=['10-26-26','14-35-14','17-17-17','20-20-3','28-28','DAP','Urea']
            st.success(f"{fertilizer_names[a]} fertilizer is recommended by the A.I for your crops.")
            
    #         array(['Urea:6', 'DAP:5', '14-35-14:1', '28-28:4', '17-17-17:2', '20-20:3',
    #    '10-26-26:0'
      

    
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)



if __name__ == '__main__':
	main()

