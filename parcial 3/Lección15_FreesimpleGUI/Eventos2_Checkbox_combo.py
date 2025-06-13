import FreeSimpleGUI as sg
layout = [
    [sg.Checkbox("Acepto terminos y condiciones", key="t&c")],
    [sg.Text("Color favorito:"), sg.Combo(["Rojo", "Azul", "Verde"], key="Color")],
    [sg.Button("Confirmar")]
]

Window = sg.Window("Ejemplo 2: Checkbox + Combo", layout, font=("Arial", 20))

while True:
    evento,valores = Window.read()
    if evento == "Confirmar" :
        t_c = valores["t&c"]
        color = valores ["Color"]
        if t_c:
            texto_terminos="El usuario acepto terminos y condiciones"
        else:
            texto_terminos="El usuario no acepto terminos y valores"
        sg.popup(f"{texto_terminos}, y selecciono el color {color}")
    elif evento == sg.WIN_CLOSED:
        break

    Window.close()

