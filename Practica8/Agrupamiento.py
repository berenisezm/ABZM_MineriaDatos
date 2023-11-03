import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Leer archivo csv
df = pd.read_csv("Practica2/datos_limpios.csv")

# Selecciona las columnas que se van a utilizar
data = df[['Goles local', 'Goles visitante']].values

# Definir los valores para k
k_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crear una gráfica para cada valor de k
for k in k_values:
    # Crea el modelo de k-means
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_
    
    # Crear la gráfica de dispersión
    plt.figure()
    
    # Dividir los datos en grupos según el número de clústeres
    for i in range(k):
        cluster_data = data[labels == i]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {i + 1}')
    
    # Dibujar los centroides de los clústeres
    plt.scatter(centroids[:, 0], centroids[:, 1], c='g', marker='X', s=100, label='Centroids')
    
    plt.xlabel('Goles local')
    plt.ylabel('Goles visitante')
    plt.legend()
    
    # Guarda las gráficas
    plt.title(f'K-Means (k={k})')
    plt.savefig(f'Practica8/grafica_k{k}.png')  
    plt.close() 