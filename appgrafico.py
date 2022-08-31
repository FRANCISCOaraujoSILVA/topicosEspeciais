import streamlit as st
import numpy as np
import plotly.graph_objects as go
with open("style.css") as p:
    st.markdown(f"<style>{p.read()}<\style>", unsafe_allow_html=True)

st.title(":sunglasses:")
# Função1 = st.latex(r'''200 \times \sqrt(2) \times \sin(2 \times \pi \times 60 \times t''')
# Função2 = st.latex(r'''(200 \times \sqrt(2) \times \sin(2 \times \pi \times 60 \times t)^2''')
st.sidebar.title('*Menu Inicial*')
varpagina = st.sidebar.selectbox('Selecione a função para visualizar o gráfico:', [":neckbeard:", ":alien:"])
if varpagina == ":neckbeard:":
    x = st.slider('Domínio', min_value=0.00000000001, max_value=0.1, step=0.00001)
    color = st.color_picker('Cores', '#00f900')
    t = np.linspace(0, x, 1000)
    v1 = 220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)
    fig1 = go.Figure(data=go.Scatter(x=t, y=v1))
    fig1.data[0].line.color = color
    st.latex(r'''200 \times \sqrt(2) \times \sin(2 \times \times \pi \times 60 \times t''')
    st.plotly_chart(fig1)

elif varpagina == ":alien:":
    x = st.slider('Domínio', min_value=0.00000000001, max_value=0.1, step=0.00001)
    color = st.color_picker('Cores', '#D20A41')
    t = np.linspace(0, x, 1000)
    v2 = (220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)) ** 2
    fig2 = go.Figure(data=go.Scatter(x=t, y=v2))
    fig2.data[0].line.color = color
    st.latex(r'''(200 \times \sqrt(2) \times \sin(2 \times \times \pi \times 60 \times t)^2''')
    st.plotly_chart(fig2)

"""
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
"""
# obs.: Uma forma de escrever as fórmulas simbólicas é escrever: streamlit.latex
