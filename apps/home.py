import streamlit as st
from apps.system_2d import exec_system_2d

def app():
    st.title('Sistema de clustering para factores de exito critico')

    st.write("Este es un prototipo de un sistema que permita visualizar clusters de los datos de investigacion")

    st.markdown("## Seleccione el algoritmo de clustering")

    algoritmo = st.selectbox("Seleccione un algoritmo de clustering", ["K-Modes","K-Medoids","GMM"])
    
    if algoritmo == "K-Modes":
        exec_system_2d('K-Modes')
    elif algoritmo == "K-Medoids":
        exec_system_2d("K-Medoids")
    elif algoritmo == 'GMM':
        exec_system_2d("GMM")