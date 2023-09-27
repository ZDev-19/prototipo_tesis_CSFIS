import streamlit as st
from apps.system import exec_system_2d,exec_system_3d

def app():
    st.title('Sistema de clustering para factores de exito critico')

    st.write("Este es un prototipo de un sistema que permita visualizar clusters de los datos de investigacion")

    css = """<style>
            .stApp {
                max-width: 100% !important;
                height: 100%
                margin: 0 !important;
                padding: 0 !important;
            }
            </style>
            """

    # Inyectar el CSS personalizado en la aplicación
    st.write(css, unsafe_allow_html=True)

    col1 , col2 = st.columns([1,2])

    with col1:
        st.markdown("## Seleccione el algoritmo de clustering")

        algoritmo = st.selectbox("Seleccione un algoritmo de clustering", ["K-Modes","K-Medoids","GMM"])

        n_cluster = st.text_input("Numero de clusters: " , "")

        n_cluster  = 2 if n_cluster == "" else int(n_cluster)

        opt = ["2D","3D"]        

        seleccion = st.radio("Tipo de grafico: " , opt)

    with col2:
        if seleccion == '2D':
            if algoritmo == "K-Modes":
                exec_system_2d('K-Modes',n_cluster)
            elif algoritmo == "K-Medoids":
                exec_system_2d("K-Medoids",n_cluster)
            elif algoritmo == 'GMM':
                exec_system_2d("GMM",n_cluster)
        elif seleccion == '3D':
            if algoritmo == "K-Modes":
                exec_system_3d('K-Modes',n_cluster)
            elif algoritmo == "K-Medoids":
                exec_system_3d("K-Medoids",n_cluster)
            elif algoritmo == 'GMM':
                exec_system_3d("GMM",n_cluster)