import FreeSimpleGUI as sg
layout=[
    [sg.Checkbox("Aceptar terminos",key="T%C")  ],
    [sg.Text("Color favorito"),sg.Combo(["Rojo", "Azul", "Verde"],key="color")],
    [sg.Button("confirmar")]
]
window=sg.Window("ejemplo 2 checkbox + combo",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento=="confirmar":
        t_c = valores["T%C"]
        color = valores["color"]
        if t_c:
            texto_terminos="el usuario ACEPTO terminos y condiciones"
        else:
            texto_terminos="el usuario NO ACEPTO terminos y condiciones"
        sg.popup(f"{texto_terminos}, y selecciono el color de {color}")
    elif evento == sg.WIN_CLOSED:
        break

window.close()