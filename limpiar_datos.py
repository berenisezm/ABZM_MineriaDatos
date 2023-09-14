import pandas as pd

# Cargar el archivo tipo csv
df = pd.read_csv("archivo.csv")

# Llenar espacios en blanco
df['Goles local'].fillna(0, inplace=True)
df['Goles visitante'].fillna(0, inplace=True)

# Cambiar el tipo de dato de la columna 'Fecha' y agregar el formato de la fecha
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%Y')

# Cambiar el tipo de dato de la columna 'Goles local' a entero y cambiar los valores no válidos por NaN
df['Goles local'] = pd.to_numeric(df['Goles local'], errors='coerce')

df = df.dropna(subset=['Goles local']) # Elimina las filas con valores NaN 

df['Goles local'] = df['Goles local'].astype(int) # Convertir la columna 'Goles local' a números enteros

# Cambiar el tipo de dato de la columna 'Goles visitante' a entero y cambiar los valores no válidos por NaN
df['Goles visitante'] = pd.to_numeric(df['Goles visitante'], errors='coerce')

df = df.dropna(subset=['Goles visitante']) # Elimina las filas con valores NaN 

df['Goles visitante'] = df['Goles visitante'].astype(int) # Convertir la columna 'Goles visitante' a números enteros

#Guardar archivo con los datos limpios
df.to_csv("datos_limpios.csv", index=False)

