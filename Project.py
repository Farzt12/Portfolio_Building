import streamlit as st 
import pandas as pd
import numpy as np

def tampilkan():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    st.line_chart(data)

    st.markdown("### Filter Data")
    range_slider = st.slider("Pilih range nilai:", 0, 100, (25, 75))
    st.write(f"Anda memilih range: {range_slider}")