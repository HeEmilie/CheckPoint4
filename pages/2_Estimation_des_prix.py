import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# configuration de la fenêtre streamlit
st.set_page_config(
    page_title="Le Domaine des Croix - étude de marché", # titre de la page
    page_icon=":grapes:",                                     # icône de la page
    layout="centered",                                      # affichage 'large' sur la page
    initial_sidebar_state="expanded",                   # statut de la barre latérale = "étendue"
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )

# --------------------------------
# IMPORT DES DATAFRAME
# --------------------------------

df_croix = pd.read_csv(r'C:\Emilie\Pro\WCS\pythonProject\checkPoint_4\csv\df_croix.csv', index_col=0)

# --------------------------------
# IMPORT DES PICKLE
# --------------------------------

with open(r'C:\Emilie\Pro\WCS\pythonProject\checkPoint_4\pickle\modelGBR.pkl', 'rb') as file:
    modelGBR = pickle.load(file)

with open(r'C:\Emilie\Pro\WCS\pythonProject\checkPoint_4\pickle\scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# --------------------------------
#
# --------------------------------

cola, colb, colc = st.columns(3)

with cola:
    st.write('')
with colb:
    image = Image.open('C:/Emilie/Pro/WCS/pythonProject/checkPoint_4/images/domaine-des-croix.jpg')
    st.image(image)
with colc:
    st.write('')

st.markdown("<h3 style='text-align: center; color: black;'>PREMIERE ESTIMATION DES PRIX</h1>",
            unsafe_allow_html=True)

st.write('En se basant sur les notes et les millésimes des crus, on peut établir la grille de prix suivante :')

X = df_croix[['points', 'millesime']]
X_scaled = scaler.transform(X)


y_pred = modelGBR.predict(X_scaled)
df_croix['price'] = y_pred
df_croix['price'] = df_croix['price'].apply(lambda x: round(x, 2))

df_1 = df_croix[['title', 'points', 'millesime', 'price']].set_index('title')
df_1 = df_1.sort_values(by='title', ascending=False)

st.dataframe(df_1)
