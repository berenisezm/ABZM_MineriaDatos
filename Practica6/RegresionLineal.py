import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Leer archivo csv
df = pd.read_csv('Practica2/datos_limpios.csv')

# Cambiar la columna Fecha a tipo de dato datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Crear la columna de Mes 
df['Mes'] = df['Fecha'].dt.to_period('M')

# Agrupar por mes y calcular la suma de goles para cada mes
datos_mes = df.groupby('Mes')[['Goles local', 'Goles visitante']].sum()

# Crear otro DataFrame con los datos de los goles
x = datos_mes['Goles local'].values.reshape(-1, 1)
y = datos_mes['Goles visitante']

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos
modelo.fit(x, y)

# Hacer predicciones con el modelo
predicciones = modelo.predict(x)

# Hacer una gráfica
plt.scatter(x, y, label="Datos reales")
plt.plot(x, predicciones, color="red", label="Regresión lineal")
plt.xlabel("Goles locales por mes")
plt.ylabel("Goles visitantes por mes")
plt.legend()
plt.savefig("Practica6/grafica.png")
