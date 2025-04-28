mensajes = "Ingresa una tare: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar, listar/salir: ")
    accion_usuario = accion_usuario.strip ()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensajes)
            todos.append(todo)
        case "mostrar"  |  "listar"
            for elemetos in todos : 