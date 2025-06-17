import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("Acepto terminos y condiciones", key="tyc")],
    [sg.Tex("color favorito:"),sg.Combo(['Rojo', 'Azul', 'Verde'],key="color")],
    [sg.Button("confrimar")]

]

Window = sg.Window("Ejemplo 2: Checkbox + Combo",layout,font=("arial",20))

while True:
    evento,valores = Window.read()
    if evento == "confirmar" :
        t_c = valores["tyc"]
        color = valores["color"]
        if t_c:
            texto_terminos="El usuario ACEPTO terminos y condiciones"
        else:
            texto_terminos="El usuario NO ACEPTO terminos y condiciones"
            sg.popup(f"{texto_terminos}, y selecciono el color:{color}")
    elif evento == sg.WIN_CLOSED:
        break

Window. close()

