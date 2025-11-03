# menampilkan judul dan deskripsi praktikum
from turtle import pd
import pandas as pd
import numpy as np
import streamlit as st
st.title("Praktikum 01 Visualisasi Data")
st.caption("Bagian 2: Data elements")
st.subheader("Bagian 1")
st.markdown("""
            Kelompok 10:
            - Ahmad Al-Faqih Asasi - 0110222190
            - Muhammad Rizky Ramadhan - 0110222184
            - Salsabila Putri Ramadhani - 0110222175
            - Fadhila Nurul Aini - 0110222166
            """)


# Data Frame
st.subheader("DataFrame")
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)


st.dataframe(df)
st.subheader("Highlight minimum values in DataFrame")
st.dataframe(df.style.highlight_min(axis=0))

#Tabel Statis
st.subheader("Tabel Statis")
df2 = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10))
)
st.dataframe(df2)

#metrics tunggal
st.subheader("metrics")
#metrics tunggal
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")
#kenaikan_suhu = 1.2 °C

col1, col2, col3 = st.columns(3)

col1.metric("curah hujan", "80 mm", "-20 mm")
col2.metric(label="populasi", value="123 Miliar", delta="1 Miliar",
            delta_color="inverse")
col3.metric("pelanggan", value=100, delta=10,
            delta_color="off")

st.metric(label="Speed", value=None, delta=0)
st.metric(label="Trees", value="91456", delta="-113649")