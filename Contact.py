import streamlit as st

def tampilkan_kontak():
    st.title("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/muhammadfarisalqodri/)"
    )
    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/username)"
    )
    # Email
    st.markdown(
        "[![Email](https://img.shields.io/badge/Email-Contact-blue)](farisalqodri@gmail.com)"
    )
    # WhatsApp
    st.markdown(
        "[![WhatsApp](https://img.shields.io/badge/WhatsApp-Contact-blue)](https://wa.me/6281234567890)"
    )

