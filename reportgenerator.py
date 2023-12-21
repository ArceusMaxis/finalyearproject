import csv
from operator import index
import streamlit as st
#import plotly.express as px
#from pycaret.regression import setup, compare_models, pull, save_model, load_model
#import pandas_profiling
from ydata_profiling import ProfileReport
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 

if os.path.exists('./dataset.csv'): 
    df = pd.read_csv('dataset.csv', index_col=None)

st.set_page_config(page_title="AutoML for Data Preprocessing")

with st.sidebar: 
    st.title("Data Preprocessing")
    st.divider()
    st.header("Report Generator")
    choice = st.radio("Navigation",["Upload","Report"], captions = ["Load Datasets", "Reports & Exports"], label_visibility="collapsed")
    st.info("Kindly upload your CSV file and then proceed to navigate to 'Report' tab to generate relevant analysis.")
    st.divider()
    st.caption("  Made by :violet[**Amirtha Krishnan**], :blue[**Sachin**] & :green[**Yekanthavasan**] - 2023")

if choice == "Upload":
    st.title("Upload Your Dataset")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df)

if choice == "Report": 
    st.title("Dataset Report")
    st.info("Scroll to find relevant dataset infographics")
    profile_df = df.profile_report()
    st_profile_report(profile_df)
    export = profile_df.to_html()
    st.download_button(label="Export Report (HTML)", data=export, file_name='report.html')

    




