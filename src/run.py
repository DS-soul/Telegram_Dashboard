# import pandas as pd
import json

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from PIL import Image

# Login SignUp
login_option = st.sidebar.radio('Login | SingUp', ('Login', 'Singup'))

# Login
if login_option == 'Login':
    with st.sidebar.form("Login"):
        st.write("Telegram dashboard")
        st.text_input('username:')
        st.text_input('password:', type='password')

        submited = st.form_submit_button('Login')
        if submited:
            pass
# SignUp
else:
    with st.sidebar.form("SignUP"):
        st.write("Telegram dashboard")
        st.text_input('Email:')
        st.text_input('username:')
        st.text_input('password:', type='password')

        submited = st.form_submit_button('SignUp')
        if submited:
            pass

# Banner
logo = Image.open('./data/9f7a508cd560347b53b41f33b95a052d.png')
st.image(logo)
# Title
st.title(':zap: Telegram Dashboard')

# Metrics
st.metric(label="Sirk o Safar si4", value="4 Members", delta="2 Online Members")

# User Info
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name: ')
    col2.text_input('Location: ')
    st.camera_input("Take a picture", key='camera_input')

# Statistics of Group
with st.expander('📊 Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.rand(100), ax=ax)
    st.pyplot(fig)

# Get infromation from User
uploaded_file = st.file_uploader('⤴️Choose a file')
if uploaded_file is not None:
    pass
    # stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
    # string_data = stringio.read()
    # st.write(string_data)

    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)







if __name__ == '__main__':
    pass