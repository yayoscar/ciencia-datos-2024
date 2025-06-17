import  FreeSimpleGUI as dx

layout = [
    [dx.Text("¿Que quieres hacer? ")],
    [dx.Button("Saludar 1"),dx.Button("Saludar 2"),dx.Button("salir")]
]

window = dx.Window("Ejemplo 3:Multiples botones",layout,font=("Arial",20))

while True:
    evento,valores = window.read()
    if evento == "Saludar 1":
        dx.popup("Hola este es un saludote jeje")
    elif evento == "Saludar 2":
        dx.popup("Esto es un saludo")
    elif evento == dx.WIN_CLOSED or evento=="Salir":
        break

window.close()