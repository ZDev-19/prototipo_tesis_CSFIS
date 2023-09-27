# Librerias de interfaz y datos
import streamlit as st
import pandas as pd

#Importacion de modelos de ML
from models.k_modes import doKModes
from models.k_medoids import doKMedoids
from models.gmm import doGMM

#Imporacion de reduccion y visualizaciones
from functions.reduccion import reducirMCA
from functions.visualizaciones import visualizar2D
from functions.visualizaciones import visualizar3D

def exec_system_2d(model,clusters):
    data = pd.read_csv("./data/CSFIS_DEF.csv")
    componentesPrincipales = reducirMCA(X = data,n_components=2) 
    
    clust_labels = None

    if model == 'K-Modes':
        clust_labels = doKModes(data,ncluster=clusters)
    elif model == 'K-Medoids':
        clust_labels = doKMedoids(componentesPrincipales,ncluster=clusters)
    elif model == 'GMM':
        clust_labels = doGMM(componentesPrincipales, n_components=clusters)

    idx = pd.DataFrame(clust_labels)
    idx= idx.rename(columns = {0: 'Cluster'}, inplace = False)

    fig = visualizar2D(componentesPrincipales,idx,'CP1','CP2')
    st.pyplot(fig)

def exec_system_3d(model,clusters):
    data = pd.read_csv("./data/CSFIS_DEF.csv")
    componentesPrincipales = reducirMCA(X = data,n_components=3) 
    
    clust_labels = None

    if model == 'K-Modes':
        clust_labels = doKModes(data,ncluster=clusters)
    elif model == 'K-Medoids':
        clust_labels = doKMedoids(componentesPrincipales,ncluster=clusters)
    elif model == 'GMM':
        clust_labels = doGMM(componentesPrincipales, n_components=clusters)

    idx = pd.DataFrame(clust_labels)
    idx= idx.rename(columns = {0: 'Cluster'}, inplace = False)

    fig = visualizar3D(componentesPrincipales,idx,'CP1','CP2','CP3')
    st.pyplot(fig)
