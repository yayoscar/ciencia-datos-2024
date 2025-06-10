import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("acepto terminos y condiciones",key="t&c")],
    [sg.Text("Color favorito:"), sg.Combo(['Azul','Rosa','verde'], key="color")],
    [sg.Button("confirmar")]
]

window = sg.Window("Ejemplo 2: Checkbox + combo", layout, font=('Bodoni MT', 20))

while True:
    eventos,valores = window.read()
    if eventos == "confirmar":
        t_c = valores["t&c"]
        color = valores["color"]
        if t_c:
            texto_terminos="el ususario no acepto terminos y condiciones"
        else:
            texto_terminos="el usuario NO ACEPTO terminos y condiciones"
        sg.popup(f"{texto_terminos}, y eselecciono el color: {color}")
    elif    eventos == sg.WIN_CLOSED:
        break

window.close()