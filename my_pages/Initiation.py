import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def run_page1():

    tab1, tab2, tab3, tab4 = st.tabs(["Title&Code", "Text&Array", "Other", "pyplot"])

    with tab1:

        st.title('Introduction à Streamlit')
        st.header('Test')
        st.subheader('Ceci est un test')

        st.markdown("""
                    ```js
                    const test_md = await markdown.wait();
            console.log("Ceci est un morceau de code en markdown:", test_md);
            ```
            """)

    with tab2:

        col1, col2 = st.columns(2)

        with col1:
            st.write("""
                    Le Lorem Ipsum est simplement du faux texte employé dans la 
                    composition et la mise en page avant impression. Le Lorem Ipsum 
                    est le faux texte standard de l'imprimerie depuis les années 1500, 
                    quand un imprimeur anonyme assembla ensemble des morceaux de texte 
                    pour réaliser un livre spécimen de polices de texte. Il n'a pas fait
                    que survivre cinq siècles, mais s'est aussi adapté à la bureautique 
                    informatique, sans que son contenu n'en soit modifié. Il a été popularisé 
                    dans les années 1960 grâce à la vente de feuilles Letraset contenant des 
                    passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des 
                    applications de mise en page de texte, comme Aldus PageMaker.
                    """)

        path = Path('assets/titanic/test.csv')
        test = pd.read_csv(path)

        with col2:
            st.dataframe(test)
            
    with tab3:

        if st.button('Ceci est un bouton'):
            st.text("Vous venez de cliquer sur le bouton!")

        if st.checkbox('Case à cocher'):
            st.text("Et là vous avez coché une case, incroyable")
        input = st.text_input('Ecrivez quelque chose')
        if input != "":
            st.text(f"{input} ? Intéressant !")
        option = st.selectbox(
            "Choisissez un chiffre",
            ("", "un", "deux", "trois"),
        )
        if option == "un":
            st.text(f"Ok donc vous votre chiffre fétiche c'est le 1 donc ?")
        elif option == "deux":
            st.text(f"Ok donc vous votre chiffre fétiche c'est le 2 donc ?")
        elif option == "trois":
            st.text(f"Ok donc vous votre chiffre fétiche c'est le 3 donc ?")

        num = st.slider("De 0 à 100", 0.0, 100.0)
        if num != 0.0 and num != 100:
            st.text(f"{num} ? Peux mieux faire !")
        elif num == 100:
            st.text(f"{num} ? Boom, maximum atteint !")

        with st.expander("Lire le texte"):
            st.write('''
                Le Lorem Ipsum est simplement du faux texte employé dans la 
                    composition et la mise en page avant impression. Le Lorem Ipsum 
                    est le faux texte standard de l'imprimerie depuis les années 1500, 
                    quand un imprimeur anonyme assembla ensemble des morceaux de texte 
                    pour réaliser un livre spécimen de polices de texte. Il n'a pas fait
                    que survivre cinq siècles, mais s'est aussi adapté à la bureautique 
                    informatique, sans que son contenu n'en soit modifié. Il a été popularisé 
                    dans les années 1960 grâce à la vente de feuilles Letraset contenant des 
                    passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des 
                    applications de mise en page de texte, comme Aldus PageMaker.
            ''')

    with tab4:
        freq = 15000

        # temps en seconde
        T = 2  # secondes
        fs = 44100  # Hertz

        # t = np.arange(T*fs)/fs
        t = np.arange(0, T, 1/fs)
        y = np.sin(2*np.pi*freq*t)

        # Tracé de la courbe
        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.set_xlim(0, 0.005)
        st.pyplot(fig)

