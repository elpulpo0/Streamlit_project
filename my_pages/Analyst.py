import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_page3():
    st.title("🕵️‍♂️ Data Analyst")
    
    st.subheader('🔄 Chargement de données')
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type='csv')
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("🔍 **Contenu du fichier CSV :**")
        st.dataframe(data)
        
        st.subheader('📊 Exploration des données')
        st.write("Premières lignes du DataFrame :")
        st.dataframe(data.head())
        
        st.write("Statistiques descriptives :")
        st.dataframe(data.describe())
        
        selected_columns = st.multiselect("Sélectionnez les colonnes à afficher", data.columns)
        if selected_columns:
            st.dataframe(data[selected_columns])
        
        st.subheader('📈 Visualisation interactive')
        col_x = st.selectbox("Choisissez une colonne pour l'axe X", data.columns)
        col_y = st.selectbox("Choisissez une colonne pour l'axe Y", data.columns)
        
        if col_x and col_y:
            st.write(f"**Nuage de points entre {col_x} et {col_y}**")
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=data, x=col_x, y=col_y, color='#1f77b4')
            st.pyplot(plt)

        st.subheader('🔍 Filtrage des données')
        filter_column = st.selectbox("Choisissez une colonne pour filtrer", data.columns)
        filter_value = st.text_input("Entrez la valeur à filtrer")
        
        if filter_value:
            filtered_data = data[data[filter_column] == filter_value]
            st.write("Données filtrées :")
            st.dataframe(filtered_data)

        st.subheader('📊 Histogramme')
        hist_column = st.selectbox("Choisissez une colonne numérique pour l'histogramme", data.select_dtypes(include=['float64', 'int64']).columns)
        num_bins = st.slider("Nombre de bacs de l'histogramme", min_value=5, max_value=100, value=30)
        
        if hist_column:
            plt.figure(figsize=(10, 6))
            sns.histplot(data[hist_column], bins=num_bins, kde=True, color='#ff7f0e')
            st.pyplot(plt)

        st.subheader('📋 Résumé des données')
        st.write("Types de données et valeurs manquantes :")
        buffer = pd.DataFrame(data.dtypes, columns=["Type de données"])
        buffer["Valeurs manquantes"] = data.isnull().sum()
        st.dataframe(buffer)

