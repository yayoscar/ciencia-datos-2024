import csv
import os




def datos_csv(nombre_archivo,datos,datos_usuario=None):

    archivo = os.path.isfile(nombre_archivo)

    with open(nombre_archivo,mode='a',newline='',encoding='utf-8') as f:
        respuestas = csv.writer(f)
        if not archivo and datos_usuario:
            respuestas.writerow(datos_usuario)
        respuestas.writerow(datos)

def leer_gastos_desde_csv(archivo):
    gastos = []
    if not os.path.isfile(archivo):
        return gastos
    with open(archivo, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['Monto'] = float(row['Monto'])
                gastos.append(row)
            except ValueError:
                print(f"Advertencia: Monto inválido en la fila: {row}. Fila omitida.")
            except KeyError as e:
                print(f"Advertencia: Columna '{e}' no encontrada en la fila: {row}. Revisar encabezados.")
    return gastos


def verificar_archivo(archivo, datos):
    if not os.path.isfile(archivo):
        with open(archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(datos)