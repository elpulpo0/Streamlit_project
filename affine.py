import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('Streamlit Project')
st.header('Fonction affine')
st.subheader('Utilisez les curseurs pour modifier les paramètres')

a = st.slider("A : De -10 à 10", -10.0, 10.0, (5.0))
b = st.slider("B : De -10 à 10", -10.0, 10.0, (-5.0))

choix_couleur = st.selectbox(
        "Choisissez la couleur de la courbe",
        ("red", "blue", "green"),
    )

x = np.linspace(-10, 10, 100)
y = a * x + b

fig, ax = plt.subplots()
ax.plot(x, y, color=choix_couleur)
ax.set_xlabel('x')
ax.set_ylabel('y')
st.pyplot(fig)

st.text(f"L'équation actuellement affichée sur le graphique est y = {a}x + {b}")
