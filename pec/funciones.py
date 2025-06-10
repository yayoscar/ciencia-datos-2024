import json

def registrar_aporte(entrada):
    return float(entrada)

def guardar_datos_en_archivo(datos):
        with open("Dato_meta_ahorro.json", "w") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

def cargar_datos_json (nombre_archivo):
    with open (nombre_archivo, "r") as cargar_archivo:
        datos = json.load(cargar_archivo)
    return datos