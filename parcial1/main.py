mensaje = "Ingresa una tarea"
todos = []
while True:
    accion_usuario=("indica que accion quieres realizar agregar/mostrar: ")
    match accion_usuario:
        case "agregar":
            todo = input(mensaje)
            todos.apped(todo)
        case "mostar":
            print(todos)
