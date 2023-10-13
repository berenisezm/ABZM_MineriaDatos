import pandas as pd
from scipy import stats

# Leer archivo csv
df = pd.read_csv('Practica2/datos_limpios.csv')

# Calcular la diferencia de goles entre equipos locales y visitantes
df['Diferencia de Goles'] = df['Goles local'] - df['Goles visitante']

# Realizar una prueba t Student para determinar si la diferencia es significativa
t_statistic, p_value = stats.ttest_1samp(df['Diferencia de Goles'], 0)

# Imprimir los resultados
print('\nPrueba t student')
print(f'Estadística t: {t_statistic}')
print(f'Valor p: {p_value}')

# Determinar si la diferencia es significativa
alpha = 0.05  # Nivel de significancia
if p_value < alpha:
    print('La diferencia de goles es significativa.')
else:
    print('No hay evidencia de una diferencia significativa en los goles.')


# Comparar las puntuaciones de goles entre diferentes jornada
jornadas = df['Jornada'].unique()
grupo_datos = [df[df['Jornada'] == jornada]['Goles local'] for jornada in jornadas]

# Realizar un ANOVA
f_statistic, p_value = stats.f_oneway(*grupo_datos)

# Imprimir los resultados
print('\nANOVA')
print(f'Estadística F: {f_statistic}')
print(f'Valor p: {p_value}')

# Determinar si hay diferencias significativas entre los grupos
alpha = 0.05  # Nivel de significancia
if p_value < alpha:
    print('Existen diferencias significativas entre los grupos.')
else:
    print('No hay evidencia de diferencias significativas entre los grupos.')