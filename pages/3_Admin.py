import streamlit as st

# configuration de la fenêtre streamlit
st.set_page_config(
    page_title="Le Domaine des Croix - étude de marché",  # titre de la page
    page_icon=":grapes:",  # icône de la page
    layout="wide",  # affichage 'large' sur la page
    initial_sidebar_state="expanded",  # statut de la barre latérale = "étendue"
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# # mise en place de la demande de mot de passe
# def check_password():
#     """Returns `True` if the user had the correct password."""
#
#     def password_entered():
#         """Checks whether a password entered by the user is correct."""
#         if st.session_state["password"] == st.secrets["password"]:
#             st.session_state["password_correct"] = True
#             del st.session_state["password"]  # don't store password
#         else:
#             st.session_state["password_correct"] = False
#
#     if "password_correct" not in st.session_state:
#         # First run, show input for password.
#         st.text_input(
#             "Mot de passe", type="password", on_change=password_entered, key="password"
#         )
#         return False
#     elif not st.session_state["password_correct"]:
#         # Password not correct, show input + error.
#         st.text_input(
#             "Mot de passe", type="password", on_change=password_entered, key="password"
#         )
#         st.error("❌ Erreur de mot de passe")
#         return False
#     else:
#         # Password correct.
#         return True
#
#
# if check_password():

st.markdown("<h1 style='text-align: center; color: black;'>MON APPROCHE</h1>",
            unsafe_allow_html=True)
st.write('')

st.markdown("<h3 style='text-align: left; color: black;'>1. VENDANGE DES DONNEES</h3>",
            unsafe_allow_html=True)

st.markdown('* récupération de la base de données du catalogue fourni  \n'
            '* étude de la base de données sous forme de dataframe  \n'
            '* remplacement des valeurs manquantes sur la colonne `country`  \n'
            '* suppression des lignes contenant encore des NaN pour les colonnes `country`, `price`, `province`, `variety`  \n'
            '* extraction des millésimes depuis la colonne `title` _(RegEx)_  \n'
            '* extraction des tokens de mots de la colonne `description`')

st.markdown("<h3 style='text-align: left; color: black;'>2. FERMENTATION DES DONNEES</h3>",
            unsafe_allow_html=True)

st.markdown('* mise en place de la structure de l\'application _(Streamlit)_  \n'
            '* réalisation des nuages de mots  \n'
            '* réalisation des graphiques')

st.markdown("<h3 style='text-align: left; color: black;'>3. MATURATION DES DONNEES</h3>",
            unsafe_allow_html=True)

st.markdown('* première étape du machine learning  \n'
            '>* détermination de la cible _(le prix dans la colonne `price`)_ et des données à partir desquelles prédire le prix _(colonnes `points` et `millesime`)_  \n'
            '>* standardisation des données avec `StandardScaler`  \n'
            '>* utilisation de `LazyPredictRegressor` pour déterminer le meilleur modèle à utiliser :  \n'
            '>> _GradientBoostingRegressor_  \n'
            '>> _$r^2$ = 0.54174 (score médiocre)_')
st.markdown('* deuxième étape du machine learning  \n'
            '>* prédiction du prix à partir de `points`, `millesime`, `country`, `variety`  \n'
            '>* encodage des colonnes `country` et `variety`  \n'
            '>* test du `DecisionTreeClassifier  \n'
            '>> _échec (score de 0.11522)_  \n'
            '>* test du `RandomForestRegressor`  \n'
            '>> _échec (score de 0.28294)_  \n')
st.markdown('* axes de progrès :  \n'
            '>* standardiser les données  \n'
            '>* partir sur un modèle de régression (choix avec `LazyPredict`, puis `GridSearch` ou `RandomSearch` pour l\'optimisation des hyperparamètres)')
