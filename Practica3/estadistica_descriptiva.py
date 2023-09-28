import pandas as pd

# Leer archivo csv
df = pd.read_csv("Practica2/datos_limpios.csv")

# Obtener el máximo en la columna de Goles local
max_goles_local = df["Goles local"].max()
print("Cantidad máxima de goles por equipos locales: ", max_goles_local)

# Obtener el máximo en la columna de Goles visitante
max_goles_visit = df["Goles visitante"].max()
print("Cantidad máxima de goles por equipos visitantes: ", max_goles_visit)

# Calcular el promedio de goles marcados por el equipo local y visitante
prom_goles_local = df.groupby('Equipo local')['Goles local'].mean()
prom_goles_visitante = df.groupby('Equipo visitante')['Goles visitante'].mean()

# Obtener los  equipos con más goles en promedio
local_mas_goles = prom_goles_local.idxmax()
visitante_mas_goles = prom_goles_visitante.idxmax()
print("Equipo local con más goles en promedio: ", local_mas_goles)
print("Equipo visitante con más goles en promedio: ", visitante_mas_goles)
print("\n")

# Contar los partidos por competencia
competencia = df['Competicion'].value_counts()
print("Cantidad de partidos por competencia")
print(competencia.to_string(name=False))
print("\n")

# Sumar la cantidad de goles que hubo por competencia
goles_competencia = df.groupby('Competicion')[['Goles local', 'Goles visitante']].sum()
print("Cantidad de goles por competencia")
print(goles_competencia)
print("\n")

# Convertir los datos a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True)

# Crear columna de año
df['Año'] = df['Fecha'].dt.year

# Hacer conteo de los partidos por año
partidos_año = df['Año'].value_counts().sort_index()
print("Cantidad de partidos por año", partidos_año.to_string(name=False))



