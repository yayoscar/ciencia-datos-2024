UTILIZÉ CHAT GPT Y META IA

pregunta:

como imprimir la info dada por el usuario:

Meta IA dijo:

Imprimir la Información Dada por un Usuario con PySimpleGUI

Para imprimir la información dada por un usuario con PySimpleGUI, puedes utilizar un elemento Multiline para mostrar la información en una ventana. A continuación, te presento un ejemplo de cómo puedes hacerlo:
import PySimpleGUI as sg

# Define el layout
layout = [
    [sg.Text('Nombre'), sg.Input(key='-NOMBRE-')],
    [sg.Text('Apellido'), sg.Input(key='-APELLIDO-')],
    [sg.Text('Edad'), sg.Input(key='-EDAD-')],
    [sg.Button('Enviar')],
    [sg.Multiline(size=(40, 10), key='-OUTPUT-')]
]

# Crea la ventana
window = sg.Window('Imprimir Información', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Enviar':
        # Obtiene la información del usuario
        nombre = values['-NOMBRE-']
        apellido = values['-APELLIDO-']
        edad = values['-EDAD-']

        # Muestra la información en la ventana
        output = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}"
        window['-OUTPUT-'].update(output)

# Cierra la ventana
window.close()
En este ejemplo, se crea una ventana con campos para ingresar el nombre, apellido y edad. Cuando se hace clic en el botón "Enviar", se obtiene la información del usuario y se muestra en un elemento Multiline en la misma ventana.

Recuerda que debes utilizar el método update para actualizar el contenido del elemento Multiline. Además, puedes personalizar el tamaño y el estilo del elemento Multiline según tus necesidades.

Otra Opción: Utilizar un Popup

Si deseas mostrar la información en una ventana emergente en lugar de en la misma ventana, puedes utilizar un popup de PySimpleGUI. A continuación, te presento un ejemplo de cómo puedes hacerlo:
import PySimpleGUI as sg

# Define el layout
layout = [
    [sg.Text('Nombre'), sg.Input(key='-NOMBRE-')],
    [sg.Text('Apellido'), sg.Input(key='-APELLIDO-')],
    [sg.Text('Edad'), sg.Input(key='-EDAD-')],
    [sg.Button('Enviar')]
]

# Crea la ventana
window = sg.Window('Imprimir Información', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Enviar':
        # Obtiene la información del usuario
        nombre = values['-NOMBRE-']
        apellido = values['-APELLIDO-']
        edad = values['-EDAD-']

        # Muestra la información en un popup
        output = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}"
        sg.popup(output, title='Información')

# Cierra la ventana
window.close()
En este ejemplo, se muestra la información en un popup cuando se hace clic en el botón "Enviar". El popup se cierra automáticamente cuando se hace clic en "OK".

YO: Me ayudo a entender la basa de como sacar información, aunque no use el popup

pregunta:

¿Cómo puedo hacer una función que sume números que da el usuario?

chat gpt dijo:

Puedes hacer una función que reciba una lista de números o que lea los números uno por uno. Aquí hay dos formas:

✅ Opción A: Recibiendo una lista de números
python
Copiar
Editar
def sumar_numeros(lista):
    return sum(lista)

# Ejemplo de uso
numeros = [10, 20, 30]
resultado = sumar_numeros(numeros)
print("Total:", resultado)

YO:esta no me sirvió, mo la supe ejecutar


✅ Opción B: Pidiendo números uno por uno
python
Copiar
Editar
def pedir_y_sumar():
    total = 0
    while True:
        entrada = input("Ingresa un número (o 'x' para salir): ")
        if entrada.lower() == 'x':
            break
        try:
            total += float(entrada)
        except ValueError:
            print("⚠️ Ingresa un número válido.")
    return total

YO: esta SI la pude ejecutar de acuerdo al contexto en el que estoy

# Ejecutar
resultado = pedir_y_sumar()
print("Suma total:", resultado)

pregunta:
2.¿Cómo puedo hacer una función que cree un archivo .csv con información?

Chat gpt dijo:

Puedes usar el módulo csv para eso. Aquí va un ejemplo que crea un archivo si no existe y agrega nuevas filas:

python
Copiar
Editar
import csv
import os

def guardar_datos(nombre, cantidad, fecha):
    archivo = "datos.csv"
    archivo_existe = os.path.exists(archivo)

    with open(archivo, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not archivo_existe:
            writer.writerow(["Nombre", "Cantidad", "Fecha"])  # encabezados
        writer.writerow([nombre, cantidad, fecha])

YO:esto me sirvió para crear el archivo csv que me pidieron y ya poder guardar la info (le pedi ayuda en mi contexto, en un 50% hice la función "guardar_gasto()")

Pregunta:

3.¿Qué otros módulos puedo usar además de csv y PySimpleGUI?

chat gpt dijo:

Aquí tienes una tabla con módulos útiles para tareas comunes relacionadas con procesamiento de datos, interfaces y validación:

Propósito	Módulo recomendado	Uso común
Trabajar con fechas	datetime	Validar y formatear fechas, calcular diferencias de días
Validar datos	re o pydantic	Validar formatos (fechas, correos, números), asegurar tipos de datos
Contar y agrupar valores	collections, defaultdict	Contar ocurrencias, acumular totales por categoría sin errores por claves faltantes
Análisis de datos/tablas	pandas	Leer y manipular archivos .csv como si fueran tablas (suma, filtrado)
Crear interfaces gráficas	PySimpleGUI	Crear ventanas interactivas para ingresar y mostrar datos
Guardar como Excel	openpyxl, pandas	Exportar datos a formato .xlsx con hojas, estilos, etc.
Formatear salida de datos	tabulate	Mostrar listas y tablas en formato legible por consola

pregunta:

4.📌 ¿Qué hace collections.defaultdict exactamente?

chat gpt dijo:

defaultdict es una variante de dict que crea automáticamente un valor por defecto si accedes a una clave que no existe. 

YO:Aquí me sirvio para entender algunos módulos que podia usar para mi programa y hacerlo mas eficiente

pregunta:

como puedo cambiar el tema de color en PySimpleGUI 


ChatGPT dijo:

En PySimpleGUI, puedes cambiar el tema de color fácilmente utilizando la función:

python
Copiar
Editar
sg.theme('NombreDelTema')
📌 Consejo
Puedes probar varios temas y elegir el que mejor se adapte a tu diseño. Algunos populares:

'DarkBlue3'

'DarkAmber'

'LightGrey1'

'SystemDefault'

'Topanga'

YO:esto me sirvio para cambiar de color mi GUI

En resumen, la IA me ayudo bastante a comprender y mejorar mi interfaz, no supe hacer una función (guardar_gasto) del todo, asi que la intente comprender y despues ya la hice. También quiero aclarar que pedí ayuda a compañeros que les toco el mismo proyecto o diferente (no sabia que hacer si el usuario no ponia tal cosa), pero despues comprendí como hacerlo



