from operator import index
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

with st.sidebar: 
    st.set_page_config(page_title="AutoML for Data Preprocessing")
    choice = st.radio("Navigation", ["Upload","Profiling"])
    st.info("Kindly upload your CSV file and then proceed to navigate to 'Profiling' tab to generate relevant analysis.")
    st.divider()
    st.caption("  Made by :violet[**Amirtha Krishnan**], :blue[**Sachin**] & :green[**Yekanthavasan**] - 2023")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Profiling": 
    st.title("Exploratory Data Analysis")
    profile_df = pandas_profiling.ProfileReport(df,lazy = False)
    st_profile_report(profile_df)
    export = profile_df.to_html()
    st.download_button(label="Export Report (HTML)", data=export, file_name= "report.html")








