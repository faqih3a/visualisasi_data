import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("Bar Chart")
st.write("Kelompok 10")
st.markdown("""
            Kelompok 10:
            - Ahmad Al-Faqih Asasi - 0110222190
            - Haura Tsabitah - 0110222242
            - Muhammad reza Pahlevi Harahap - 0110122110
            """)

st.graphviz_chart("""
digraph {
    "Tranining Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Results Forecating"
    "New Data" -> "Model"
    }
""")