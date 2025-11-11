import streamlit as st
import pandas as pd
import numpy as np

st.title("Map Chart")
st.write("Kelompok 10")
st.markdown("""
            Kelompok 10:
            - Ahmad Al-Faqih Asasi - 0110222190
            - Haura Tsabitah - 0110222242
            - Muhammad reza Pahlevi Harahap - 0110122110
            """)

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=['latitude', 'longitude']
)

st.map(df)