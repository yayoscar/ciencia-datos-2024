import FreeSimpleGUI as sg
import csv
import os

def guardar_gastos(ventana, fecha, monto, categoria):
    write_header = not os.path.exists('datos.csv')
    with open('datos.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(['fecha', 'monto', 'categoria'])
        writer.writerow([fecha, monto, categoria])
    ventana['-STATUS-'].update('Datos guardados correctamente.')
    return
