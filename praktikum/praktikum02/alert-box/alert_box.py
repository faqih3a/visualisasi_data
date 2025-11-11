# menampilkan judul dan deskripsi praktikum
from turtle import pd
import pandas as pd
import numpy as np
import streamlit as st
st.title("Praktikum 02 Visualisasi Data")
st.subheader("Bagian 3: Alert Box")
st.markdown("""
            Kelompok 10:
            - Ahmad Al-Faqih Asasi - 0110222190
            - Haura Tsabitah - 0110222242
            - Muhammad reza Pahlevi Harahap - 0110122110
            """)

st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception(Exception("It is an exception"))