import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("Practica2/datos_limpios.csv")

# Combinar las columnas Equipo visitante y Equipo local
equipos = df['Equipo visitante'] + ' ' + df['Equipo local']

# Combinar los nombres de los equipos en un solo texto
texto_equipos = ' '.join(equipos.astype(str))

# Crear la nube de texto
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_equipos)

# Guardar la nube de texto
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.savefig("Practica10/nube_texto.png")