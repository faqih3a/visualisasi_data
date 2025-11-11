import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.write("Kelompok 10")
st.markdown("""
            Kelompok 10:
            - Ahmad Al-Faqih Asasi - 0110222190
            - Haura Tsabitah - 0110222242
            - Muhammad reza Pahlevi Harahap - 0110122110
            """)

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=['c1', 'c2', 'c3', 'c4']
)

st.bar_chart(df)
