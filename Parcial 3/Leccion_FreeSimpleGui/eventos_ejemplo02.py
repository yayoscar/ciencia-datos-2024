import FreeSimpleGUI as sg
from FreeSimpleGUI import Checkbox
layout = [
    [sg.Checkbox("Acepto Términos y condiciones",key="t&c")],
    [sg.Text("Color favorito"),sg.Combo(["Rojo","Verde","Azul"],key="color")],
    [sg.Button("Confirmar")]
]

window = sg.Window("Ejemplo 2: Checkbox + Combo",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento=="Confirmar" :
        t_c = valores["t&c"]
        color = valores["color"]
        if t_c :
            texto_terminos = "El usuario ACEPTO términos y condiciones"
        else:
            texto_terminos = "El usuario NO ACEPTO términos y condiciones"
        sg.popup(f"{texto_terminos},y selecciono el color: {color}")
    elif evento == sg.WIN_CLOSED:
        break

window.close()