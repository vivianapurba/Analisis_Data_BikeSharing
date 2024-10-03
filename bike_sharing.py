import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import scipy.stats as stats

st.set_page_config(page_title="Bike Sharing", layout="wide")
st.title("Bike Sharing Dashboard by Viviana Purba")
st.markdown("---")
# Load cleaned data
bikesharing_clean = all_df = pd.read_csv("bikesharing_clean.csv")

# Create a container for the plots
container = st.container()

with container:
    # Plot 1: Tren Rental Sepeda pada Tahun 2011-2012
    total_count_by_year = all_df.groupby(['year', 'month'])['total_count'].sum().reset_index()
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='month', y='total_count', hue='year', data=total_count_by_year, palette=['blue', 'red'], markers=['o', 's'])
        ax.set_xlabel('Bulan')
        ax.set_ylabel('Jumlah Sepeda yang Dirental')
        ax.set_title('Tren Rental Sepeda pada Tahun 2011-2012')
        ax.legend(loc='upper right')
        ax.set_xticks(range(1, 13))
        st.pyplot(fig)

    # Plot 2: Perubahan Total Sepeda yang Dirental dalam Seminggu
    category = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    avg_weekday = all_df.groupby('weekday')['total_count'].mean()
    with col2:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=category, y=avg_weekday, palette=['gray' if x != max(avg_weekday) else 'orange' for x in avg_weekday])
        ax.set_xlabel('Hari')
        ax.set_ylabel('Total Rata-Rata Sepeda yang dirental')
        ax.set_title('Perubahan Total Sepeda yang Dirental dalam Seminggu')
        st.pyplot(fig)

    st.markdown("---")

    # Plot 3: Perbedaan Penggunaan Rental Sepeda antara Hari Libur dan Hari Biasa
    avg_holiday = all_df[all_df['holiday'] == 1]['total_count'].mean()
    avg_non_holiday = all_df[all_df['holiday'] == 0]['total_count'].mean()
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.bar(['Hari Libur', 'Hari Biasa'], [avg_holiday, avg_non_holiday])
        ax.set_xlabel('Jenis Hari')
        ax.set_ylabel('Rata-Rata Total Sepeda yang Dirental')
        ax.set_title('Perbedaan Penggunaan Rental Sepeda antara Hari Libur dan Hari Biasa')
        st.pyplot(fig)

    st.markdown("---")

    # Plot 4: Total rental sepeda dalam 1 hari berdasarkan musim
    with col2:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(data=all_df[['hour','total_count','season']],x='hour',y='total_count',hue='season',ax=ax, palette='Set1')
        ax.set(title="Total rental sepeda dalam 1 hari berdasarkan musim")
        ax.set_xlabel('Jam')
        ax.set_ylabel('Total rental sepeda')
        ax.legend(loc='upper right')
        ax.set_xticks(range(0, 24))
        st.pyplot(fig)
