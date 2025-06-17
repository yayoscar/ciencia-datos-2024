import  FreeSimpleGUI as sg

layout=[
    [sg.Text("ingrese su nombre"),sg.Input(key="nombre")],
    [sg.Button("mostrar",button_color=("white","red"))]
]
window=sg.Window("",layout,font=("Arial",20))

while True:
    event ,values=window.read()
    if event=="mostrar":
        print(event, values)
        sg.popup(f"Hola!, Tu nombre es:  {values["nombre"]}")
    elif event == sg.WIN_CLOSED:
        break
