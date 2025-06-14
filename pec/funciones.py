import csv
import os

def guardar_gastos(ventana, fecha, monto, categoria):
    write_header = not os.path.exists('datos.csv')
    with open('datos.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(['fecha', 'monto', 'categoria'])
        writer.writerow([fecha, monto, categoria])
    ventana['-STATUS-'].update('Datos guardados correctamente.\n')
    return

def mostrar_datos(archivo):
    if not os.path.exists(archivo):
        return "No hay datos registrados aún."

    with open(archivo, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        filas = list(reader)

    if len(filas) <= 1:
         return "No hay gastos registrados aún."

    encabezado = filas[0]
    datos = filas[1:]

    contenido = "LISTA DE GASTOS:\n\n"
    for i, fila in enumerate(datos, start=1):
        fecha, monto, categoria = fila
        contenido += f"{i}. Fecha: {fecha or 'Sin fecha'}, Monto: ${monto}, Categoría: {categoria}\n"

    return contenido