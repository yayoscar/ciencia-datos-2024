mensaje = "Ingresa una tarea: "
todos = []
while True:
    accion_usuario=input("Indica que acción quieres realizar agregar/mostar/salir ")
    acccion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            for elemento in todos:
             print(elemento)
        case "salir":
            break
print("Adios")
