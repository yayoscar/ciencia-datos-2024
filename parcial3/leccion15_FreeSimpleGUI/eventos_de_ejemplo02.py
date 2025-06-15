import FreeSimpleGUI as sg

layout = [
   [sg.Checkbox("Acepto Término y condiciones",key="t_y_c")],
   [sg.Text("color favorito:").sg.combo(['Rojo','Azul','Verde'],key="color")],
   [sg.Button("confirmar")]
]

window = sg.window("Ejemplo 2: checkbox + combo",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento == "confirmar" :
        t_c = valores["t_y_c"]
        color = valores["color"]
        if t_c:
            texto_terminos="El usuario ACEPTO términos y condiciones"
        else:
            texto_terminos = "el usuario NO ACEPTO  térmonos y condiciones"
        sg.popup(f"{texto_terminos}, y selecciono el color: {color}")
    elif evento == sg.WIN_CLOSED:
        break
        window.close()