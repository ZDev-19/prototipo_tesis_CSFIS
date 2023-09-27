import seaborn as sns
from mpl_toolkits import mplot3d 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import streamlit as st

# Visualizacion 2D
def visualizar2D(principalDf,idx,tituloEjeX,tituloEjeY):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Datos para puntos en 2D
    scatter = ax.scatter(principalDf[0],principalDf[1],c=idx['Cluster'],s=50)
    ax.set_xlabel(tituloEjeX)
    ax.set_ylabel(tituloEjeY)
    plt.colorbar(scatter)

    return fig

# Visualizacion 2D con titulos
def visualizar2DconTitulosCluster(principalDf,idx,tituloEjeX,tituloEjeY):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # id de grupos
    cantidadClusters=idx['Cluster'].nunique()
    targets=list(range(cantidadClusters))
    colors= list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(cantidadClusters)))
    #targets = [0, 1, 2]
    #colors=['blue','green','red']
    for target, color in zip(targets, colors):
    # se relaciona el id del grupo con un color
        indicesToKeep = idx['Cluster'] == target
    # se relaciona los datos con el id del grupo y color 
    ax.scatter(principalDf.loc[indicesToKeep, 1]
    , principalDf.loc[indicesToKeep, 2]
    , c=color
    , s=50)
    ax.legend(targets)
    ax.set_xlabel(tituloEjeX)
    ax.set_ylabel(tituloEjeY)

    return fig

# Visualizacion 3D
def visualizar3D(principalDf,idx,tituloEjeX,tituloEjeY,tituloEjeZ):
    fig = plt.figure(figsize=(8, 6), dpi=80)
    ax = fig.add_subplot(111, projection='3d')
    
    # Obtener la lista de clusters únicos y asignar colores aleatorios a cada uno
    clusters_unicos = idx['Cluster'].unique()
    colores = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(clusters_unicos))]
    
    for cluster, color in zip(clusters_unicos, colores):
        # Seleccionar las filas del cluster actual
        indices = idx['Cluster'] == cluster
        
        # Obtener los datos para los ejes X, Y y Z
        x = principalDf.loc[indices, 0]
        y = principalDf.loc[indices, 1]
        z = principalDf.loc[indices, 2]
        
        # Graficar los puntos del cluster actual en el gráfico 3D
        ax.scatter(x, y, z, c=color, label=f'Cluster {cluster}')

    # Configurar etiquetas de ejes y leyenda
    ax.set_xlabel(tituloEjeX)
    ax.set_ylabel(tituloEjeY)
    ax.set_zlabel(tituloEjeZ)
    ax.legend()

    return fig
