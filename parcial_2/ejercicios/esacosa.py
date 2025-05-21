mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()
    match accion_usuario:
        case "agregar" | "añadir":
            todo = input(mensaje)
            todo = f"{todo}n"
            archivo = open("todos.txt", "r")
            todos = archivo.readlines()
            archivo.close()
            todos.append(todo)
            archivo = open("todos.txt", "m")
            archivo.writelines(todos)
            archivo.close()
        case "mostrar" | "listar":
            archivo = open("todos.txt", "r")
            todos = archivo.readlines()
            archivo.close()
            for indice, elemento in enumerate(todos):
                elemento = elemento.title()
                print(f"{indice+1}--{elemento}", end="**")
        case "editar":
            indice= int(input("Ingrese el número de la lista a editar: "))
            nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
            todos[indice-1] = nueva_tarea
        case "completar":
            indice = int(input("Ingrese el número de la lista a completar: "))
            indice -= 1
            todos.pop(indice)
            archivo = open("todos.txt", "m")
            archivo.writelines(todos)
            archivo.close()
        case "salir":












