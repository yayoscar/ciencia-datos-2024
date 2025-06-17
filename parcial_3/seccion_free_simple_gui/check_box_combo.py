import FreeSimpleGUI as sg

layout = [
    [sg.Checkbox("Aceptar terminos y condiciones",key='T&C')],
    [sg.Combo(['Azul','Rojo','Verde'],key='color')],
    [sg.Button('Confirmar')]

]

window = sg.Window("Ejemplo02: Checkbox + Combo",layout,font=('Britannic Negrita',30))

while True:
    evento,values = window.read()
    if evento =='confirmar':
        t_c = values['T&C']
        color = values['color']
        if t_c:
            texto_terminos ="El usuario ACEPTO terminos y condiciones"
        else:
            texto_terminos = "El usuario NO ACEPTO terminos y condiciones"
        sg.popup(f"{texto_terminos}, y selecciono el color: {color}")
    elif evento == sg.WIN_CLOSED:
        break

window.close()