import streamlit as st
from apps.system import exec_system

def app():
    st.title('Sistema de recomendacion de factores de exito critico')

    st.write("Este es un prototipo de un sistema que le recomendara ciertos factores")

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

    df_rec = None

    with col1:
        st.header("Asigna tus propios ratings")

        ip = st.select_slider(
            'Califica el factor Infraestructura Politica',
            options=[1,2,3,4,5]
        )

        ca = st.select_slider(
            'Califica el factor Control de Accesos',
            options=[1,2,3,4,5]
        )

        gr = st.select_slider(
            'Califica el factor Gestion del riesgo',
            options=[1,2,3,4,5]
        )

        am = st.select_slider(
            'Califica el factor Auditoria y Monitoreo',
            options=[1,2,3,4,5]
        )

        dc = st.select_slider(
            'Califica el factor Desarrollo de competencias',
            options=[1,2,3,4,5]
        )

        cn = st.select_slider(
            'Califica el factor Continuidad del Negocio',
            options=[1,2,3,4,5]
        )

        ge = st.select_slider(
            'Califica el factor Gestion de externos',
            options=[1,2,3,4,5]
        )

        cc = st.select_slider(
            'Califica el factor Cultura y concientizacion',
            options=[1,2,3,4,5]
        )

        gee = st.select_slider(
            'Califica el factor Gestion del equipo encargado',
            options=[1,2,3,4,5]
        )

        pe = st.select_slider(
            'Califica el factor Prioridades y Estructura',
            options=[1,2,3,4,5]
        )

        if st.button('Enviar',type="primary"):
            inputs = [ip,ca,gr,am,dc,cn,ge,cc,gee,pe]
            df_rec = exec_system(inputs)

    with col2:
        st.dataframe(df_rec)
