import FreeSimpleGUI as fd


layaut = [
    [fd.Text("NOmbre"),fd.Input(key="mnombre")],
    [fd.Button("mostrar")]
]

window = fd.Window("mostrar nombre ingresado", layaut, font=("arial",20))

while True:
    event, values = window.read()
    if event == "mostrar":
        print(event, values)
        fd.popup(f"hola, Tu nombre es {values['nombre']}")
    elif event == fd.WIN_CLOSED:
        break