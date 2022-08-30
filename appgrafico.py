import streamlit as st
import numpy as np
import plotly.graph_objects as go
with open("style.css") as p:
    st.markdown(f"<style>{p.read()}<\style>", unsafe_allow_html=True)

st.title(":sunglasses:")

#
st.sidebar.title('*Menu Inicial*')
varpagina = st.sidebar.selectbox('Selecione a função para visualizar o gráfico:', ['Função 1', 'Função 2'])
if varpagina == 'Função 1':
    x = st.slider('Domínio', min_value=0.00000000001, max_value=0.1, step=0.00001)
    color = st.color_picker('Cores', '#00f900')
    t = np.linspace(0, x, 1000)
    v1 = 220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)
    fig1 = go.Figure(data=go.Scatter(x=t, y=v1))
    fig1.data[0].line.color = color
    st.markdown('*Função 1:*')
    st.markdown('*220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)*')
    st.plotly_chart(fig1)

elif varpagina == 'Função 2':
    x = st.slider('Domínio', min_value=0.00000000001, max_value=0.1, step=0.00001)
    color = st.color_picker('Cores', '#D20A41')
    t = np.linspace(0, x, 1000)
    v2 = (220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)) ** 2
    fig2 = go.Figure(data=go.Scatter(x=t, y=v2))
    fig2.data[0].line.color = color
    st.markdown('*Função 2:*')
    st.markdown('*(220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)) ** 2*')
    st.plotly_chart(fig2)


