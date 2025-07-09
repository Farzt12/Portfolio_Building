import streamlit as st

st.set_page_config(page_title=
                   "Portfolio Building", page_icon=":rocket:", layout="wide")
st.title("Portfolio Building")
st.header("Data Scientist and Developer Portfolio")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", 
                        ["About Me", "Project", "Machine Learning", "proses", "Contact"])

if page == "Contact":
    import Contact
    Contact.tampilkan_kontak()
elif page == "About Me":
    import About
    About.tampilkan_tentang()
elif page == "Project":
    import Project
    Project.tampilkan()
elif page == "Machine Learning":
    import Prediction
    Prediction.prediksi()
elif page == "proses":
    import Predict
    Predict.proses()    