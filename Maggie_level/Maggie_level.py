import requests
import time
import json
import csv

while True:
  url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
  r = requests.get(url)
  response = r.json()
  datos: str = response
  completo = datos[0]
  frase = completo['quote']
  personaje = completo['character']
  cita = frase + " " + personaje
  print(cita)
  
  cita = {"quote": frase, "character": personaje}

  if personaje == "Lisa Simpson":
    with open('Lisa/Lisa.csv', 'a+') as f:
      wr = csv.DictWriter(f, cita.keys())
      wr.writerow(cita)
      
      

  elif personaje == "Homer Simpson":
    with open('Homer/Homer.csv', 'a+') as f:
     wr = csv.DictWriter(f, cita.keys())
     wr.writerow(cita)
     
  else:
    
    with open('General/General.csv', 'a+') as f:
      wr = csv.DictWriter(f, cita.keys())
      wr.writerow(cita)
      
      
    

      time.sleep(30)

