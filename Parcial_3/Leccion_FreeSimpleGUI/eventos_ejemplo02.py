import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("Acepto términos y condiciones", key= 'tyc')],
    [sg.Text("Color favorito"), sg.Combo(['Verde', 'Rojo', 'Azul'], key= 'color')],
    [sg.Button('Confirmar')]
]

window = sg.Window("Términos y color", layout, font=('Arial', 20))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event== 'Confirmar':
        aceptado = values['tyc']
        if aceptado:
            texto_aceptado = "Sí"
        else:
            texto_aceptado = "No"
        fav = values['color']
        sg.popup(f"Aceptó los términos y condiciones: {texto_aceptado} \nColor favorito: {fav}", title="Sé donde vives", font=('Arial', 15))

window.close()