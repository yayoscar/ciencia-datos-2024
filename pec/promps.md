Dime paso a paso como puedo crear  archivo csv 
que guarde los datos que un usuario ingreso al usar  
un código de Python que usa FreeSimpleGUI

Perfecto! Ya que te refieres a FreeSimpleGUI 
(probablemente quisiste decir PySimpleGUI,
una biblioteca muy popular para interfaces gráficas en Python),
aquí tienes una guía paso a paso para:

> 📌 Crear un archivo .csv que guarde los datos que un 
> usuario ingresa usando una interfaz gráfica hecha con PySimpleGUI.
✅ Requisitos previos
Primero, asegúrate de tener instalado PySimpleGUI:
pip install PySimpleGUI
🧩 Paso a Paso
1. Crea un formulario con PySimpleGUI
El siguiente código crea una ventana donde el usuario puede ingresar datos:
import PySimpleGUI as sg
import csv
# Define los campos del formulario
layout = [
    [sg.Text("Nombre"), sg.InputText(key='NOMBRE')],
    [sg.Text("Edad"), sg.InputText(key='EDAD')],
    [sg.Text("Correo"), sg.InputText(key='CORREO')],
    [sg.Button("Guardar"), sg.Button("Salir")]
]
# Crea la ventana
ventana = sg.Window("Formulario de Usuario", layout)
Lógica para guardar en CSV
Añade el siguiente código después de crear la ventana:
# Archivo CSV donde se guardarán los datos
archivo_csv = 'usuarios.csv'
# Escribe encabezados si el archivo no existe
try:
    with open(archivo_csv, 'x', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['Nombre', 'Edad', 'Correo'])
except FileExistsError:
    pass  # Ya existe el archivo
# Bucle de eventos
while True:
    evento, valores = ventana.read()
    
    if evento == sg.WIN_CLOSED or evento == "Salir":
        break
    
    if evento == "Guardar":
        nombre = valores['NOMBRE']
        edad = valores['EDAD']
        correo = valores['CORREO']

        # Guarda los datos en el archivo CSV
        with open(archivo_csv, 'a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow([nombre, edad, correo])
        
        sg.popup("Datos guardados correctamente")

# Cierra la ventana
ventana.close()
📁 Resultado
Este código creará un archivo llamado usuarios.csv con este formato:
Nombre,Edad,Correo
Ana,23,ana@gmail.com
Carlos,30,carlos@outlook.com
Cada vez que el usuario rellene el formulario y presione "Guardar",
se añadirá una nueva línea al archivo.
✅ Personalización
Puedes:
Cambiar o agregar campos fácilmente en el layout.
Validar entradas (números, correos, etc.) antes de guardarlas.
Guardar el archivo en otra carpeta: cambia 'usuarios.csv' por
'datos/usuarios.csv', por ejemplo.

Y como lo puedo hacer con una función?

¡Buena idea! Encapsular el guardado de datos en una función
te da un código más limpio, reutilizable y fácil de mantener.

A continuación te muestro cómo puedes adaptar el ejemplo
anterior de PySimpleGUI para que use una función que
guarda los datos en un archivo .csv.

✅ Paso a paso: Usar una función para guardar los datos en CSV

📁 1. Define la función para guardar los datos

import csv
import os

def guardar_en_csv(nombre_archivo, datos, encabezados=None):
    """
    Guarda una lista de valores en un archivo CSV.
    
    nombre_archivo: str → nombre del archivo (ej: 'usuarios.csv')
    datos: list     → lista con los datos del usuario, ej: ['Ana', 23, 'ana@gmail.com']
    encabezados: list (opcional) → si se da, se escriben si el archivo no existe
    """
    archivo_existe = os.path.isfile(nombre_archivo)

    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        if not archivo_existe and encabezados:
            escritor.writerow(encabezados)
        escritor.writerow(datos)
🧠 2. Usa esta función en el código de PySimpleGUI

import PySimpleGUI as sg

# Define la interfaz
layout = [
    [sg.Text("Nombre"), sg.InputText(key='NOMBRE')],
    [sg.Text("Edad"), sg.InputText(key='EDAD')],
    [sg.Text("Correo"), sg.InputText(key='CORREO')],
    [sg.Button("Guardar"), sg.Button("Salir")]
]

ventana = sg.Window("Formulario con función CSV", layout)

# Archivo donde se guardarán los datos
archivo_csv = 'usuarios.csv'
encabezados = ['Nombre', 'Edad', 'Correo']

while True:
    evento, valores = ventana.read()

    if evento == sg.WINDOW_CLOSED or evento == "Salir":
        break

    if evento == "Guardar":
        datos_usuario = [valores['NOMBRE'], valores['EDAD'], valores['CORREO']]
        guardar_en_csv(archivo_csv, datos_usuario, encabezados)
        sg.popup("Datos guardados exitosamente")

ventana.close()
✅ Ventajas de usar una función
Si luego quieres guardar en otro archivo, solo cambias el nombre.
Puedes llamar esa función desde otros formularios o scripts.
Mejora la legibilidad y mantenimiento del código.