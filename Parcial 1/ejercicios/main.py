mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()
    match accion_usuario:
        case "agregar"|"añadir":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar"| "listar":
            for elemento in todos:
                elemento = elemento.title()
                print(elemento)
        case "salir":
            break
        case _:
            print("No entiendo esta acción.")
print("Adiós")