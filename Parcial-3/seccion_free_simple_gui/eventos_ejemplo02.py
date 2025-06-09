import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("Acepto terminos y condiciones", key="t&c")],
    [sg.Text("Color favorito"),sg.Combo(['Rojo','Azul','Verde'],key='color')],
    [sg.Button("confirmar")]
]

window = sg.Window("Ejemplo 2: Checkbox + Combo",layout,font=("Arial",20))

while True:
    event,valores = window.read()
    if event == "confirmar":
        tyc = valores["t&c"]
        color = valores["color"]
        if tyc:
            texto_terminos ="El usuario ACEPTO terminos y condiciones"
        else:
            texto_terminos = "El usuario NO ACEPTO terminos y condiciones"
        sg.popup(f"{texto_terminos}, y selecciiono el color: {color}")
    elif event == sg.WIN_CLOSED:
        break

window.close()