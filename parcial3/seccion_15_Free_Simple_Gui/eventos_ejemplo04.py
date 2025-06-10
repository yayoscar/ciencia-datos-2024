import  FreeSimpleGUI as sg

layout = [
    [sg.Text("ingrese nombre:"), sg.Input(key="nombre")],
    [sg.Text("ingrese edad"), sg.Input(key="edad")],
    [sg.Text("Lenguaje favorito"), sg.Combo(["python","Javascript","C++"])],
    [sg.Checkbox("Aspecto recibir emails", key="email")],
    [sg.Button("enviar"), sg.Button("cancelar")]
]

window = sg.Window("minimini encuesta interactiva",layout, font=("Arial", 20))

while True:
    evento, valores = window.read()
    if evento =="enviar":
        nombre=valores["nombre"]
        edad=valores["edad"]
        lenguaje=valores["lenguaje"]
        if valores["email"]:
            recibe="si"
        else:
            recibe="no"
        mensaje = f"""nombre: {nombre}
        edad: {edad}
        lenguaje favorito: {lenguaje}
        recibe emails: {recibe}"""
        sg.popup(mensaje, font=("Arial", 20))
    if evento == sg.WIN_CLOSED or evento == "cancelar":
        break

window.close()