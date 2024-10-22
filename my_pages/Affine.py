import streamlit as st
import plotly.graph_objects as go
import numpy as np

def run_page2():
    st.header("Visualisation interactive d'une fonction affine avec Streamlit")
    st.subheader('Utilisez les curseurs pour modifier les paramètres')

    col1, col2 = st.columns(2)

    with col1:
        a = st.slider("A : De -10 à 10", -10.0, 10.0, 5.0)
        b = st.slider("B : De -10 à 10", -10.0, 10.0, -5.0)

        choix_couleur = st.selectbox(
            "Choisissez la couleur de la courbe",
            ("red", "blue", "green", "orange", "purple")
        )

    with col2:
        x = np.linspace(-10, 10, 100)
        y = a * x + b

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x, 
            y=y, 
            mode='lines',
            name=f'y = {a}x + {b}',
            line=dict(color=choix_couleur, width=2)
        ))

        fig.update_layout(
            title=f'Graphique de y = {a}x + {b}',
            xaxis_title='x',
            yaxis_title='y',
            template='plotly_dark',
            margin=dict(l=0, r=0, t=40, b=40)
        )

        st.plotly_chart(fig)

    st.markdown(f"L'équation actuellement affichée sur le graphique est **y = {a}x + {b}**", unsafe_allow_html=True)