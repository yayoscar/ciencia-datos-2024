import FreeSimpleGUI as dx

layout = [
    [dx.Checkbox("Aceptar terminos y condiciones", key="T_C")],
    [dx.Text("Color favorito:"), dx.Combo(['Rojo','Azul','Verde'],key="Color")],
    [dx.Button("Confirmar")]
]

window = dx.Window("Ejemplo 2: Checkbox + Combo",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento == "Confirmar":
        T_C = valores["T_C6 "]
        Color = valores["Color"]
        if T_C:
            texto_termino="El usuario acepto terminos y condiciones"
        else:
            texto_termino = "El usuario no acepto terminos y condiciones"
        dx.popup(f"{texto_termino}, y selecciono el color: {Color}")
    elif evento == dx.WIN_CLOSED:
        break

window.close()
