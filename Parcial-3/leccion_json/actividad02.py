import json

persona = {
    "nombre": "Carlos",
    "edad": 35,
    "profesion": "Ingeniero",
    "casado": False 
}

with open("persona.json", "w") as archivo:
    json.dump(persona, archivo, indent=4)
