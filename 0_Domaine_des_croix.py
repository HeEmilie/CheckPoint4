import streamlit as st
from PIL import Image

# configuration de la fenêtre streamlit
st.set_page_config(
    page_title="Le Domaine des Croix - étude de marché", # titre de la page
    page_icon=":grapes:",                                     # icône de la page
    layout="wide",                                      # affichage 'large' sur la page
    initial_sidebar_state="expanded",                   # statut de la barre latérale = "étendue"
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )


cola, colb, colc = st.columns(3)

with cola:
    st.write('')
with colb:
    image = Image.open('images/domaine-des-croix.jpg')
    st.image(image)
with colc:
    st.write('')


col1, col2, col3 = st.columns(3)

with col1:
    image1 = Image.open('images/domaine-des-croix-beaune-1er-cru-les-bressandes-2019.jpg')
    st.image(image1)

with col2:
    image2 = Image.open('images/domaine-des-croix-beaune-1er-cru-les-greves-2017.jpg')
    st.image(image2)

with col3:
    image3 = Image.open('images/domaine-des-croix-corton-grand-cru-la-vigne-au-saint-2018.jpg')
    st.image(image3)

st.markdown("<h1 style='text-align : center; color : black; '>QUEL PRIX POUR CES CRUS SUR LE MARCHE AMERICAIN ?</h1>",
            unsafe_allow_html=True)

