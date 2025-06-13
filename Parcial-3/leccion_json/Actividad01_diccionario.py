import json

datos_json = '{"nombre": "Luis", "edad": 25, "ciudad": "Lima"}'
diccionario = json.loads(datos_json)
print(diccionario)

hobbies = ["leer","correr","jugar"]
pretty = json.dumps(hobbies)
print(pretty)