import streamlit as st

# Titre de l'application
st.title('Mon Projet Streamlit')

# Menu de navigation dans la barre latérale
st.sidebar.header('Navigation')

# Gérer l'état de session pour la page
if 'page' not in st.session_state:
    st.session_state.page = "Initiation"

# Créer des boutons pour chaque page
if st.sidebar.button("Initiation"):
    st.session_state.page = "Initiation"
if st.sidebar.button("Fonction Affine"):
    st.session_state.page = "Fonction Affine"
if st.sidebar.button("Data Analyst"):
    st.session_state.page = "Analyst"

# Importer et exécuter la page appropriée
if st.session_state.page == "Initiation":
    from my_pages.Initiation import run_page1
    run_page1()
elif st.session_state.page == "Fonction Affine":
    from my_pages.Affine import run_page2
    run_page2()
elif st.session_state.page == "Analyst":
    from my_pages.Analyst import run_page3
    run_page3()
