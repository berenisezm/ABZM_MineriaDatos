import os 
import requests


url = "https://zenodo.org/record/7860755/files/partidos_futbol.csv?download=1" # Url del archivo csv


if not os.path.exists("archivo.csv"):
    # Si el archivo no existe, hay que descargarlo
    response = requests.get(url)

    if response.status_code == 200:
        # Si la solicitud fue exitosa, se guarda el archivo
        with open("archivo.csv", "wb") as archivo:
            archivo.write(response.content)
    else:
        # Si la solicitud no fue exitosa, manda un error
        print("Error. Código de estado: {response.status_code}")

else:
    # Si el archivo ya existe, se informa que ya fue descargado
    print(f"El archivo 'archivo.csv' ya está descargado.")



