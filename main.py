import base64
import streamlit as st

st.set_page_config(
    page_title="Come i lupi amano gli agnelli",
    page_icon="🐺",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Come i lupi amano gli agnelli")
st.text("di Ivan Masnari")

with open("pdfs/Come_i_lupi_amano_gli_agnelli_e_altre_poesie.pdf", "rb") as f:
    pdf_file = f.read()    

st.download_button(label="Scarica il libro",
                    data=pdf_file,
                    file_name="come_i_lupi_amano_gli_agnelli.pdf",
                    mime='application/pdf')

#put an image to the left and a text to the right
col1, col2 = st.columns([1, 3])

with col1:
    #small image
    st.image("imgs/main_img.png")

with col2:
    st.write(
        """
        _Siedi più a me vicino,_\n
        _guardami con occhi allegri:_\n
        _ecco il quaderno azzurro_\n
        _dei miei versi infantili._\n
        \t\t\t - Achmatova
        """
    )