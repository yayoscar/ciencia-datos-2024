import FreeSimpleGUI as sg
from FreeSimpleGUI import WIN_CLOSED

layout = [
    [sg.Checkbox("Acepto términos y condiciones", key="t&c")],
    [sg.Text("Color favorito:"),sg.Combo(["Rojo", "Verde", "Azul"], key="color")],
    [sg.Button("Confirmar")]
]

window = sg.Window("Ejemplo02 - Checkbox y Combo", layout, font=("Arial", 20))

while True:
    evento, valores = window.read()
    if evento == "Confirmar":
        t_c = valores["t&c"]
        color = valores["color"]
        if t_c:
            texto_terminos = "El susuario ACEPTO términos y condiciones"
        else:
            texto_terminos = "El usuario NO ACPETO términos y condiciones"
        sg.popup(f"{texto_terminos}, y slecciono el color: {color}")
    elif evento == sg.WIN_CLOSED:
        break

window.close()