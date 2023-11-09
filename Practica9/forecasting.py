import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datetime import datetime

# Cargar el archivo CSV
df = pd.read_csv("Practica2/datos_limpios.csv")

# Asegúrate de que la columna 'Fecha' esté en un formato de fecha adecuado
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Agrega una nueva columna para el mes
df['Mes'] = df['Fecha'].dt.month

# Agrupa los datos por mes y calcula el total de goles en cada mes
goles_por_mes = df.groupby(['Mes'])[['Goles local', 'Goles visitante']].sum().reset_index()

# Divide tus datos en conjuntos de entrenamiento y prueba
X = goles_por_mes[['Mes']]
y_local = goles_por_mes[['Goles local']]
y_visitante = goles_por_mes[['Goles visitante']]
X_train, X_test, y_local_train, y_local_test = train_test_split(X, y_local, test_size=0.2, random_state=0)
X_train, X_test, y_visitante_train, y_visitante_test = train_test_split(X, y_visitante, test_size=0.2, random_state=0)

# Entrena dos modelos de regresión lineal, uno para goles locales y otro para goles visitantes
model_local = LinearRegression()
model_local.fit(X_train, y_local_train)
model_visitante = LinearRegression()
model_visitante.fit(X_train, y_visitante_train)

# Genera predicciones para el año 2024
months_2024 = [i for i in range(1, 13)]  # De enero a diciembre del 2024
predicted_goles_local = model_local.predict(np.array(months_2024).reshape(-1, 1))
predicted_goles_visitante = model_visitante.predict(np.array(months_2024).reshape(-1, 1))

# Crea dos gráficas separadas, una para goles locales y otra para goles visitantes

plt.figure(figsize=(8, 6))
plt.scatter(X, y_local, label='Goles Local', color='blue', marker='o', alpha=0.7)
plt.plot(months_2024, predicted_goles_local, label='Regresión', color='blue')
plt.xticks(months_2024, [datetime(2024, month, 1).strftime('%b') for month in months_2024])
plt.xlabel('Mes 2024')
plt.ylabel('Goles Local')
plt.title('Predicción de Goles Locales en el Año 2024')
plt.legend()
plt.savefig("Practica9/grafica_local.png")

plt.figure(figsize=(8, 6))
plt.scatter(X, y_visitante, label='Goles Visitante', color='red', marker='o', alpha=0.7)
plt.plot(months_2024, predicted_goles_visitante, label='Regresión', color='red')
plt.xticks(months_2024, [datetime(2024, month, 1).strftime('%b') for month in months_2024])
plt.xlabel('Mes 2024')
plt.ylabel('Goles Visitante')
plt.title('Predicción de Goles Visitantes en el Año 2024')
plt.legend()
plt.savefig("Practica9/grafica_visitante.png")