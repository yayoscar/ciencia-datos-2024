mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario=input("Indica que acción quieres realizar agregar/mostrar,lista/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            for elemento in todos:
                elemento = elemento
                print(elemento)
        case "salir":
            break
        case _:

             print("No entindo esa acción")
print("adios")

