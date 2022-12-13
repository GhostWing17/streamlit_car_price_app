import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_eda_app() :
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')
    st.subheader('기본 통계 데이터')
    st.dataframe( df.describe() )
    