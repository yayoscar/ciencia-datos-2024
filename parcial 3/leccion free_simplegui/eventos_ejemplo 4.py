import  FreeSimpleGUI as sg


layout=[
    [sg.Text("nombre: "),sg.Input(key="nombre")],
    [sg.Text("edad"),sg.Input(key="edad")],
    [sg.Text("lenguaje favorito: "), sg.Combo(["python","java","c++"],
                                              key="lenguaje")],
     [sg.Checkbox("aceto recibir emails", key="email")],
    [sg.Button("Enviar"), sg.Button("Cancelar")]
 ]

window=sg.Window("encuesta",layout)

while True:
    evento,valores=window.read()
    if evento =="enviar":
        nombre=valores["nombre"]
        edad=valores["edad"]
        lenguaje=valores["lenguaje"]
        recibe = "si " if valores["email"] else "no"
        mensaje = f"""""nombre: {nombre}
        edad {edad}
        lenguaje favorito: {lenguaje}
        recibe emails: {recibe}"""""
        sg.popup(mensaje,font=("Arial",20))
    if evento ==sg.WIN_CLOSED or evento =="cancelar":
        break
    window.close()