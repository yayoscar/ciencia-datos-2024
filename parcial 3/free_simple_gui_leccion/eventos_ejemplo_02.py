import FreeSimpleGUI as sg
from FreeSimpleGUI import popup

layout = [
    [sg.Checkbox("acepto terminos y condiciones",key="t&c")],
    [sg.Text("color favorito"),sg.Combo(['Azul','Rojo','Verde'],key="color")],
    [sg.Button("comfirmar")]

]
window = sg.Window("Ejemplo 2: checkbox + combo",layout,font=("Signpainter",20))

while True:
    evento,valores = window.read()
    if evento == "comfirmar" :
        t_c = valores["t&c"]
        color = valores["colores"]
        if  t_c:
             texto_terminos = "el usuario acepto terminos y condiciones"
        else:
         texto_terminos = "El usuario NO acepto terminos y condiciones"
        sg.popup(f"{texto_terminos},y selecciono el color{color}")
    elif evento == sg.WIN_CLOSED:
        break

window.close()
