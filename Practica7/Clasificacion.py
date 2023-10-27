import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Leer archivo csv
df = pd.read_csv('Practica2/datos_limpios.csv')

# Crear una columna para asignar valores a los equipos locales y visitantes
def Asig_valor_equipo(equipo):
    if equipo == "Equipo Local":
        return 0
    else:
        return 1

# Aplicar lo anterior en el dataframe
df["Equipo local"] = df["Equipo local"].apply(Asig_valor_equipo)
df["Equipo visitante"] = df["Equipo visitante"].apply(Asig_valor_equipo)

# Crear una columna para determinar si hubo empate
df['Empate'] = (df['Goles local'] == df['Goles visitante']).astype(int)

# Seleccionar las características para la clasificación
X = df[['Equipo local', 'Equipo visitante', 'Goles local', 'Goles visitante']]
y = df['Empate']

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Establecer los colores 
colors = ['purple' if empate == 1 else 'red' for empate in df['Empate']]

# Hacer una gráfica de dispersión 
plt.scatter(df['Goles local'], df['Goles visitante'], c=colors)
plt.xlabel('Goles Local')
plt.ylabel('Goles Visitante')
plt.title('Clasificación de Empates y No Empates')
plt.scatter([], [], c='purple', label='Empate')
plt.scatter([], [], c='red', label='No Empate')
plt.legend()
plt.savefig("Practica7/grafica.png")