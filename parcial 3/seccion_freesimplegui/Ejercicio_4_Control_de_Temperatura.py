import FreeSimpleGUI as sg

layout=[
    [sg.Slider(range=(0,100),orientation="h", key="SLIDER")],
    [sg.Button("Revisar")], [sg.Button("Cerrar")],
    [sg.Text("Temperatura", key="TEMPERATURA")]
]

window=sg.Window("Control de Temperatura", layout)
while True:
    event, values=window.read()
    temp=values["SLIDER"]
    if event== sg.WIN_CLOSED or event=="Cerrar":
        break
    elif temp<20:
        window["TEMPERATURA"].update("Frio")
    elif temp<30:
        window["TEMPERATURA"].update("Agradable")
    else:
        window["TEMPERATURA"].update("Caliente")

window.close()