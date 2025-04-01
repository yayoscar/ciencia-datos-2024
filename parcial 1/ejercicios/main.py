mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()
    match accion_usuario:
        case "agregar"|"añadir":
            todo = input(mensaje)
            todos.append(todo)
        case "mostrar"| "listar":
            for indice,elemento in enumerate(todos):
                elemento = elemento.title()
                print(f"{indice+1}--{elemento}")
        case "editar":
            indice= int(input("Ingrese el número de la lista a editar: "))
            nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
            todos[indice-1] = nueva_tarea
        case "completar":
            indice = int(input("Ingrese el número de la lista a completar: "))
            indice -= 1
            todos.pop(indice)
        case "salir":
            break
        case _:
            print("No entiendo esta acción.")
print("Adiós")