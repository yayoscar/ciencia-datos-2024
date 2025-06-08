import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("acepto terminos y condiciones",key="tyc")],
    [sg.Text("color favorito"), sg.Combo(['azul', 'rojo','verde'], key="color")],
    [sg.Button("confirmar")]
]

window = sg.Window("ejemplo 2:checkbox + combo",layout, font=("arial", 20))

while True:
    evento, valores = window.read()
    if evento == "confirmar":
        t_c = valores["tyc"]
        color = valores["color"]
        if t_c:
            texto_terminos = "el usuario ACEPTO los terminos"
        else:
            texto_terminos = "el usuarios NO ACEPTO los terminos "
        sg.popup(f"{texto_terminos}, y selecciono el color {color}")
    elif evento == sg.WINDOW_CLOSED:
        break

window.close()