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

coll1, coll2 = st.columns(2)

coll1.write("Ini adalah kolom pertama")
coll1.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyMNsjoaGyqs5FCuGvKFUbI7_88VeFJpbk4A&s")
coll2.write("Ini adalah kolom kedua")
coll2.image("https://www.viralsumsel.com/wp-content/uploads/2025/09/bahlil-lahadalia.jpg")