import pandas as pd
import streamlit as st
names_link = './content/dataset.csv'
names_data = pd.read_csv(names_link)
# Create the title for the web app
st.title("Streamlit and pandas")
st.dataframe(names_data)


sidebar = st.sidebar

sidebar.title("Luis Enrique Romero Pérez")

sidebar.write("Matricula: zs21004524.")

sidebar.image("https://firebasestorage.googleapis.com/v0/b/paradigmas-luigi196362.appspot.com/o/javascript%2Fimages%2Fcredencial.jpg?alt=media&token=ffba3513-0c65-4540-8bdf-140a9ba8f468")