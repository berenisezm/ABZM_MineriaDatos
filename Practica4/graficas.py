import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo csv
df = pd.read_csv("Practica2/datos_limpios.csv")

# Cantidad de goles anotados por cada equipo en una competición
goles_por_competicion = df.groupby("Competicion")[["Goles local", "Goles visitante"]].sum()

# Crear el gráfico de barras
goles_por_competicion.plot(kind="bar", stacked=True)
plt.title("Total de Goles por Competición")
plt.xlabel("Competición")
plt.ylabel("Total de Goles")
plt.legend(["Goles Local", "Goles Visitante"])
plt.savefig("Practica4/grafica_barras.png")


# Crear una columna de "Resultado" basada en los goles
df["Resultado"] = df.apply(lambda row: "Empate" if row["Goles local"] == row["Goles visitante"]
                           else "Victoria Local" if row["Goles local"] > row["Goles visitante"]
                           else "Victoria Visitante", axis=1)

# Contar los resultados en todos los partidos
resultados_globales = df["Resultado"].value_counts()

# Crear el gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(resultados_globales, labels=resultados_globales.index, autopct='%1.1f%%', startangle=140)
plt.title("Proporción de Resultados en Todas las Competiciones")
plt.axis('equal')  # Hace que el gráfico de pastel sea circular
plt.savefig("Practica4/grafica_pastel.png")


# Crear historama de los goles marcados por equipos locales
plt.figure(figsize=(8, 6))
plt.hist(df["Goles local"], bins=10, edgecolor='k')
plt.title("Distribución de Goles Marcados por Equipos Locales")
plt.xlabel("Goles")
plt.ylabel("Frecuencia")
plt.savefig("Practica4/histograma_locales.png")


# Crear historama de los goles marcados por equipos visitantes
plt.figure(figsize=(8, 6))
plt.hist(df["Goles visitante"], bins=10, edgecolor='k')
plt.title("Distribución de Goles Marcados por Equipos Visitantes")
plt.xlabel("Goles")
plt.ylabel("Frecuencia")
plt.savefig("Practica4/histograma_visitantes.png")


# Sumar los goles locales y visitantes por jornada
goles_por_jornada = df.groupby("Jornada")[["Goles local", "Goles visitante"]].sum()

# Crear el gráfico de líneas
plt.figure(figsize=(8, 6))
goles_por_jornada.plot()
plt.title("Evolución de Goles por Jornada")
plt.xlabel("Jornada")
plt.ylabel("Total de Goles")
plt.legend(["Goles Local", "Goles Visitante"])
plt.savefig("Practica4/grafica_lineas.png")

