import streamlit as st
import pandas as pd

from models.k_modes import doKModes
from models.k_medoids import doKMedoids
from models.gmm import doGMM

from functions.Preprocesadores import pre_min_max , pre_standar
from functions.reduccion import reducirMCA
from functions.visualizaciones import visualizar2D
import streamlit as st

def exec_system_2d(model):
    data = pd.read_csv("./data/CSFIS_DEF.csv")
    componentesPrincipales = reducirMCA(X = data) 
    
    clust_labels = None

    if model == 'K-Modes':
        clust_labels = doKModes(data,ncluster=3)
    elif model == 'K-Medoids':
        clust_labels = doKMedoids(componentesPrincipales,ncluster=3)
    elif model == 'GMM':
        clust_labels = doGMM(componentesPrincipales,n_components=3)

    idx = pd.DataFrame(clust_labels)
    idx= idx.rename(columns = {0: 'Cluster'}, inplace = False)

    fig = visualizar2D(componentesPrincipales,idx,'CP1','CP2')
    st.pyplot(fig)

