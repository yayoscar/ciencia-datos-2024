mensaje = "ingresa una tarea: "
todos= []
while True:
    accion_usuario=input("Indica que accion quieres realizar agregar?/mostrar: ")
    accion_usuario
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            print(todos)
