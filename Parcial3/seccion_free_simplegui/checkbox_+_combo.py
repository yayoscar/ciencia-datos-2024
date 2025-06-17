import FreeSimpleGUI as sg
layout =[
    [sg.Checkbox("Acepto términos y condiciones", key="t&c")],
    [sg.Txt("Color favorito:"), sg.Combo(["Rojo","Azul","Verde"], key="Color")],
    [sg.Button("Confirmar")]
]

Window = sg.Window("Ejemplo 2: Checkbox + Combo",layout,font=("Arial",25))

while True:
    evento,valores = Window.read()
    if evento == "Confirmar":
        t_c =  valores["t&c"]
        color = valores["Color"]
        if t_c:
            textp_terminos="El usuario ACEPTÓ los términos y condiciones "
        else:
            textp_terminos="El usuario NO aceptó los términos y condiciones."
        sg.popup(f"{textp_terminos}, y seleccionó el siguiente color: {color}")
    elif evento == sg.WIN_CLOSED:
        break

Window.close()

