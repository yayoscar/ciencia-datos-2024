import  FreeSimpleGUI as sg

layout=[
    [sg.Checkbox("acepta los terminos y condiciones",key="tyc")],
    [sg.Text("color favorito"),sg.Combo(["rojo","azul","verde"],key="color")],
    [sg.Button("confirmar")]
]

window=sg.Window("ejemplo_2: Checkbox + combo",layout,font=("Arial",20))


while True:
    evento,values=window.read()
    if evento== "confirmar":
        t_c=values["tyc"]
        color= values["color"]
        if t_c:
            texto_terminos="El usuario acepto terminos y condiciones"
        else:
            texto_terminos="El usuario no acepto los terminos y condiciones"
        sg.popup(f"{texto_terminos}, y seleciono el color: {color}")
    elif evento == sg.WIN_CLOSED:
        break
