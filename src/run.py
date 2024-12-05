# import pandas as pd
import streamlit as st
from io import StringIO

st.title(':zap: Telegram Dashboard')

uploaded_file = st.file_uploader('Choose a file')
# if uploaded_file is not None:
    
#     stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
#     string_data = stringio.read()
#     st.write(string_data)
    
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)







if __name__ == '__main__':
    pass