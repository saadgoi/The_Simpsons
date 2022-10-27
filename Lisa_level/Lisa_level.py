from turtle import clear
import requests
import time
import json
import csv
import os
from urllib import request

def word_count(str):
        
        counts = dictwords
        words = str.split()
        
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts

dictwords = {}

while True:
    url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    r = requests.get(url)
    response = r.json()
    datos: str = response
    completo = datos[0]
    frase = completo['quote']
    personaje = completo['character']
    imagen = completo['image']
    cita = frase + " " + personaje
    print(cita)
    dictwords = word_count(frase)
    print(dictwords)
    #print(imagen)

    
    cita = {"quote": frase, "character": personaje}
        
    archivo = personaje +'.csv'
    archivo = archivo.replace(' ','_')
    carpeta = personaje
    os.getcwd()  # busca en qué directorio se encuentra
    os.chdir("Lisa_level")
    
    with open("conteo", 'a+') as g:
            wr = csv.DictWriter(g, dictwords.keys())
            wr.writerow(dictwords)

    if not os.path.exists(carpeta):
        os.mkdir(carpeta)  # crea la carpeta
        os.chdir(carpeta)  # cambia a la carpeta creada

        with open(archivo, 'a+') as f:
            wr = csv.DictWriter(f, cita.keys())
            wr.writerow(cita)
            response = request.urlretrieve(imagen, "personaje.png")
            f.close()
             
    else:
        os.stat(carpeta)
        os.chdir(carpeta)
        with open(archivo, 'a+') as f:
            wr = csv.DictWriter(f, cita.keys())
            wr.writerow(cita)
            response = request.urlretrieve(imagen, "personaje.png")
            f.close()

    os.chdir("../")  # vuelve al directorio indicado
    time.sleep(30)
