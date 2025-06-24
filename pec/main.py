import FreeSimpleGUI as sg
import funciones

layout = [
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="-NOMBRE-")],
    [sg.Text("Precio por unidad:"),sg.Input(key="-PRECIO-")],
    [sg.Text("Veces por semana"), sg.Input(key="-VECES-")],
    [sg.Text("Meses:"), sg.Input(key="-MESES-")],
    [sg.Button("Calcular ahorro")]
]

window =sg.Window("Calculadora de gastos hormiga.Yarely 2AMCI",layout,font=("Arial",15),background_color="pink",button_color="purple",sbar_background_color="purple")
todos = []

while True:
    evento,valores = window.read()
    if evento == "Calcular ahorro":
        nombre = valores['-NOMBRE-']
        precio = valores['-PRECIO-']
        veces = valores['-VECES-']
        meses = valores['-MESES-']
        try:
            calculo = funciones.calcular(precio, veces, meses)
            window['-PRECIO-'].update(calculo)

            nueva_fila = [nombre, precio, veces, meses, str(calculo)]
            todos = funciones.leer_tareas()
            todos.append(nueva_fila)
            funciones.guardar_tareas(todos)

            sg.popup(f"Podrías ahorrar: {calculo} pesos si evitas este gasto por {meses} meses")
        except ValueError:
            sg.popup("Error: Ingresa números válidos en Precio, Veces y Meses")
    elif evento == sg.WIN_CLOSED or evento == "Salir":
        break



window.close

