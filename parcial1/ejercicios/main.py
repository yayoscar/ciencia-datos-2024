mensaje = "ingresa una tarea: "
todos = []
while True:
    accion_usuario = input("indica que accion quieres realizar agregar/mostrar,lista/salir:")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.apped(todo)
         case "mostrar" | "listar":
                   for elemento in todos:
                       elemto = elemento.title()
                       print(elemento)
        case "salir":
            break
            case _:
               


