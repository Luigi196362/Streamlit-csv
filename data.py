import pandas as pd
import streamlit as st
names_link = './content/dataset.csv'
names_data = pd.read_csv(names_link)
# Create the title for the web app
st.title("Streamlit and pandas")
st.dataframe(names_data)
