import FreeSimpleGUI as sg

layout = [
    [sg.Text("ingresa tu nombre"), sg.Input(key="Nombre")],
    [sg.Text("ingresa tu Apellido"), sg.Input(key="Apellido")],
    [sg.Text("ingresa tu email"), sg.Input(key="email")],
    [sg.Button("Enviar"), sg.Button("limpiar"), sg.Button("Salir")]
]
ventana = sg.Window("Formulario de registro",layout,font=("Arial",20))

while True:
    evento, valores = ventana.read()
    if evento == sg.WIN_CLOSED or evento == 'salir':
        break
    elif evento == "enviar":
        nombre = valores['nombre']
        apellido = valores ['apellido']
        email = valores['email']

        ventana.close()