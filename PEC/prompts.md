Paginas consultadas:
How to Import Local Modules with Python
https://www.geeksforgeeks.org/how-to-import-local-modules-with-python/
Here is how to build a GUI with FreeSimpleGUI in Python.
https://pythonhow.com/how/build-a-gui-with-freesimplegui/
How to Pass Optional Parameters to a Function in Python
https://www.geeksforgeeks.org/how-to-pass-optional-parameters-to-a-function-in-python/
Reading and Writing CSV Files in Python
https://realpython.com/python-csv/
How do I append to a file?
https://stackoverflow.com/questions/4706499/how-do-i-append-to-a-file
CSV in Python adding an extra carriage return, on Windows
https://stackoverflow.com/questions/3191528/csv-in-python-adding-an-extra-carriage-return-on-windows
Uso de ia:
como puedo hacer un pop up para que muestre una tabla en python usando freesimplegui?


ChatGPT Plus
¡Buena pregunta!
En FreeSimpleGUI (que es un fork ligero de PySimpleGUI), puedes mostrar una tabla dentro de una ventana emergente (popup) usando sg.Window. No existe un sg.popup_table directo, pero puedes crear fácilmente una ventana temporal con un sg.Table.

Aquí tienes un ejemplo funcional:

python
Copiar
Editar
import FreeSimpleGUI as sg

# Datos de ejemplo para la tabla
cabecera = ['Nombre', 'Edad', 'Ciudad']
datos = [
    ['Ana', 23, 'CDMX'],
    ['Luis', 30, 'Monterrey'],
    ['Marta', 28, 'Guadalajara'],
]

# Layout de la ventana emergente
layout = [
    [sg.Table(values=datos,
              headings=cabecera,
              auto_size_columns=True,
              justification='center',
              num_rows=min(len(datos), 10))],
    [sg.Button('Cerrar')]
]

# Crear la ventana
ventana = sg.Window('Tabla emergente', layout)

# Loop para manejar eventos
while True:
    evento, valores = ventana.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Cerrar':
        break

ventana.close()