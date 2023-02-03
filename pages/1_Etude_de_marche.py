import streamlit as st
import pandas as pd
import plotly.express as px
import random
from PIL import Image


df = pd.read_csv('csv/df_clean.csv', index_col=0)
df_pinot_noir = df[df['variety'] == 'Pinot Noir']
df_notes = pd.read_csv('csv/df_notes.csv', index_col=0)

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

tab1, tab2, tab3 = st.tabs(['Etude mondiale', 'Etude des notes', 'Pinot Noir'])

with tab1:

    col21, col22 = st.columns(2)

    with col22:
        st.markdown("<h1 style='text-align: center; color: black;'>NOMBRE DE VINS PAR PAYS</h1>",
                    unsafe_allow_html=True)

        fig_nombre = px.bar(x=df['country'].value_counts().index,
                            y=df['country'].value_counts(),
                            labels=dict(x='', y=''),
                            color_discrete_sequence=px.colors.qualitative.Antique)
        st.plotly_chart(fig_nombre, use_container_width=True)

        st.markdown("<h1 style='text-align: center; color: black;'>MEILLEURE NOTE DANS CHAQUE PAYS</h1>",
                    unsafe_allow_html=True)

        fig_best = px.bar(x=df_notes['country'],
                          y=df_notes['points_max'],
                          labels=dict(x='', y=''),
                          color_discrete_sequence=px.colors.qualitative.Antique)
        st.plotly_chart(fig_best, use_container_width=True)

    with col21:
        st.write('')
        st.write('')
        st.write('')
        image_bottle = Image.open('images/wc_world_bottle.png')

        # st.markdown("<h4 style='text-align: center; color: black;'>MOTS LES PLUS RECURRENTS DANS LES DESCRIPTIONS</h1>",
        #             unsafe_allow_html=True)

        st.image(image_bottle)





with tab2:

    st.markdown("<h1 style='text-align: center; color: black;'>REPARTITION DES NOTES PAR PAYS ET PAR CEPAGE</h1>",
                unsafe_allow_html=True)

    st.write('')
    st.write('')
    st.write('')
    st.write('')
    pays = sorted(df['country'].unique())
    selected_pays = st.selectbox('Choisissez un pays', pays, index=len(pays)-3)
    nombre_vins = len(df[df['country'] == selected_pays])
    st.write(f'Vous avez choisi {selected_pays} qui a {nombre_vins} vins dans le catalogue')
    cepage = sorted(df[df['country'] == selected_pays]['variety'].unique())
    selected_cepage = st.selectbox('Quel cépage ?', cepage, index=15)
    nombre_cep = len(df[(df['country'] == selected_pays) & (df['variety'] == selected_cepage)]['variety'])
    st.write(
        f'Parmi les vins que l\'on trouve en {selected_pays}, il y en a {nombre_cep} qui sont de type {selected_cepage}')
    st.write('')
    st.write('')
    note_moyenne_mondiale = round(df[df['variety'] == selected_cepage]['points'].mean(), 2)
    note_moyenne_par_pays = round(
        df[(df['country'] == selected_pays) & (df['variety'] == selected_cepage)]['points'].mean(), 2)
    st.write(
        f'Les vins de type {selected_cepage} ont une note moyenne de {note_moyenne_mondiale}/100 dans le monde, et de {note_moyenne_par_pays}/100 en {selected_pays}.')


    fig = px.histogram(x=df[(df['country'] == selected_pays) & (df['variety'] == selected_cepage)]['points'],
                        marginal='box',
                        labels=dict(x='', y=''),
                        color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig, use_container_width=True)


with tab3:
    st.markdown("<h1 style='text-align: center; color: black;'>CONCERNANT LE PINOT NOIR</h1>",
                unsafe_allow_html=True)

    col31, col32 = st.columns(2)

    with col31:
        st.write('')
        st.write('')
        st.write('')
        image_pinot = Image.open('images/wc_pinot.png')

        # st.markdown("<h4 style='text-align: center; color: black;'>MOTS LES PLUS RECURRENTS DANS LES DESCRIPTIONS DU PINOT NOIR</h1>",
        #             unsafe_allow_html=True)

        st.image(image_pinot)

    with col32:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        note_moyenne_pinot = round(df[df['variety'] == 'Pinot Noir']['points'].mean(), 2)
        st.write(f'Le Pinot Noir a une note moyenne de {note_moyenne_pinot}/100 dans le monde')

        #st.write(f'On le trouve parmi les pays suivants :')
        pays_pinot_noir = sorted(df_pinot_noir['country'].unique())
        selected_pinot = st.selectbox('On le trouve parmi les pays suivants :', pays_pinot_noir)
        note_moy_pinot_pays = round(df_pinot_noir[df_pinot_noir['country'] == selected_pays]['points'].mean(), 2)
        nombre_pinot = len(df_pinot_noir[df_pinot_noir['country'] == selected_pinot])

        st.write(f'En {selected_pinot}, Le Pinot Noir a une note moyenne de {note_moy_pinot_pays}/100.')
        liste_pinot = df_pinot_noir[df_pinot_noir['country'] == selected_pinot]['name'].unique()
        nb = random.randint(0, len(liste_pinot))
        st.write(f'On en trouve {nombre_pinot} différents, tels que \'{liste_pinot[nb]}\', \'{liste_pinot[nb+1]}\' ou encore \'{liste_pinot[nb-1]}\'')

    st.markdown("<h3 style='text-align: center; color: black;'>LE PINOT NOIR DE BOURGOGNE (FRANCE)</h1>",
                unsafe_allow_html=True)

    col33, col34 = st.columns(2)

    with col33:
        st.write('')
        st.write('')
        st.write('')
        image_pinot_bourgogne = Image.open('images/wc_pinot_bourgogne.png')
        st.image(image_pinot_bourgogne)

    with col34:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        note_moyenne_pinot_bourgogne = round(df[(df['variety'] == 'Pinot Noir') & (df['province'] == 'Burgundy')]['points'].mean(), 2)
        st.write(f'Le Pinot Noir de Bourgogne a une note moyenne de {note_moyenne_pinot_bourgogne}/100')

        liste_pinot_bourgogne = df[(df['variety'] == 'Pinot Noir') & (df['province'] == 'Burgundy')]['name'].unique()
        nombre_pinot_bourgogne = len(liste_pinot_bourgogne)
        nb_b = random.randint(0, len(liste_pinot))
        st.write(f'On en trouve {nombre_pinot_bourgogne} différents, tels que \'{liste_pinot_bourgogne[nb_b]}\', \'{liste_pinot_bourgogne[nb_b + 1]}\' ou encore \'{liste_pinot_bourgogne[nb_b - 1]}\'')

        fig_pb = px.histogram(x=df[(df['variety'] == 'Pinot Noir') & (df['province'] == 'Burgundy')]['points'],
                              marginal='box',
                              labels=dict(x='', y=''),
                              color_discrete_sequence=px.colors.qualitative.Antique)
        st.plotly_chart(fig_pb, use_container_width=True)
