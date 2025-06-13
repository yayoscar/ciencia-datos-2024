import json


with open("personas.json", "r") as archivo:
    personas = json.load(archivo)

for persona in personas:
    print("Nombre:", persona["nombre"])