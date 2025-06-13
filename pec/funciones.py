import csv
import os

def datos_csv(nombre_archivo,datos,datos_usuario=None):

    archivo = os.path.isfile(nombre_archivo)

    with open(nombre_archivo,mode='a',newline='',encoding='utf-8') as f:
        respuestas = csv.writer(f)
        if not archivo and datos_usuario:
            respuestas.writerow(datos_usuario)
        respuestas.writerow(datos)



