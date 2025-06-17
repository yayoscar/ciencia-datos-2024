import FreeSimpleGUI as sg
from funciones import calcular

layout = [
    [sg.Text("Nombre del gasto hormiga:"), sg.Input(key="-NOMBRE-")],
    [sg.Text("Precio por unidad:"),sg.Input(key="-PRECIO-")],
    [sg.Text("Veces por semana"), sg.Input(key="-VECES-")],
    [sg.Text("Meses:"), sg.Input(key="-MESES-")],
    [sg.Button("Calcular ahorro")]
]

window =sg.Window("Calculadora de gastos hormiga",layout,font=("Arial",15),background_color="pink",button_color="purple",sbar_background_color="purple")


while True:
    evento,valores = window.read()
    if evento == "Calcular ahorro":
        precio = valores['-PRECIO-']
        veces = valores['-VECES-']
        meses = valores['-MESES-']
        calculo = calcular(precio,veces,meses)  # Usas la función importada
        window['-PRECIO-'].update(calculo)
        sg.popup(f"Podrias ahorrar:{calculo} pesos si evitas este gasto por {meses} meses")
    elif evento == sg.WIN_CLOSED or evento == "Salir":
        break


window.read
window.close

