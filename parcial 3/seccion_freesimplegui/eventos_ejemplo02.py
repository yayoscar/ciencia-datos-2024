import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("Aceptar terminos y condiciones",key="T&C")],
    [sg.Text("Color favorito:"),sg.Combo(['Azul','Rojo','Verde'],key="color")],
    [sg.Button("Confirmar")]
    ]

window= sg.Window(title="Ejemplo 2:Checkbox + combo",layout=layout,font=("Arial",20))

while True:
    event,valores = window.read()
    if event == "Confirmar":
        t_c = valores["T&C"]
        color = valores["color"]
        if t_c:
            texto_termings="El usuario ACEPTO terminos y condiciones"
        else:
            texto_termings ="El usuario NO ACEPTO terminos y condiciones"
        sg.popup(f"{texto_termings}, y selecciono: {color}")
    elif event ==sg.WIN.CLOSED:
        break

window.close()