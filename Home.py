# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import streamlit_authenticator as stauth

def main():
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> CRFE - Farmers true friend 🧑‍🌾 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("Made by: Shivam Sunil Bhosale, Jay Gabhawala and Vishva Deliwala")
    st.write("The proposal suggests creating a Crop and Fertilizer Recommendation Engine (CFRE) that will offer farmers personalized recommendations for crop and fertilizer selection. It will use technology to consider factors like geography, climate, and soil type to optimize crop yield. The engine will gather data from a crop and fertilizer dataset, and farmers will input details about their soil, climate, and other factors to receive tailored recommendations. The proposal explains the problem statement, motivation, and potential solutions for implementing the engine")
    
    placeholder = st.empty()

    actual_email = "email"
    actual_password = "password"

# Insert a form in the container
    with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit and email == actual_email and password == actual_password:
        # If the form is submitted and the email and password are correct,
        # clear the form/container and display a success message
        placeholder.empty()
        st.success("Login successful")
    elif submit and email != actual_email and password != actual_password:
        st.error("Login failed")
    else:
        pass


if __name__ == '__main__':
	main()