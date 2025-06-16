import FreeSimpleGUI as sg
from openpyxl.chart.title import Title
from openpyxl.styles.builtins import title

layout = [
    [sg.Checkbox("Aceptar terminos y condiciones",key="t&c")],
    [sg.Text("color favorito: "),sg.Combo(['rojo','azul','verde'],key="color")],
    [sg.Button("Confirmar")]

]

window = sg.Window("Ejemplo 2: Checbox + Combo",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento == "confirmar":
        t_c = valores["t&c"]
        color = valores["color"]
        if t_c:
            texto_terminos = "el usuario acepto terminos y condiciones"
        else:
            texto_terminos= "el usuario no acepto los terminos y condiciones"
        sg.popup(f"{texto_terminos},y selecciono el color: {color}")
    elif evento == sg.WIN_CLOSED:
        break

window.close()

