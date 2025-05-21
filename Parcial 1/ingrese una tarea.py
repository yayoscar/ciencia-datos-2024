mensaje = "ingrese una tarea: "
todos = []
while True:
    accion_usuario=input("indica que accion quieres realizar agregar/mostrar: ")
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar":
            print(todos)