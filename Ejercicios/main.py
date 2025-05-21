mensaje = "Ingresa una terea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/listar/completar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()
    match accion_usuario:
        case "agregar"|"añadir":
            todo = input(mensaje)
            todo = f"{todo}\n"

            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)

        case "mostrar" | "listar":
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
                print(archivo.read())

            # todos_sin_espacio = [elemento.strip("\n") for elemento in todos]
            for indice,elemento in enumerate(todos):
                elemento = elemento.title()
                elemento = elemento.strip("\n")
                print(f"{indice+1}--{elemento}")
        case "editar":
            indice = int(input("Ingrese el número de la lista a editar: "))
            nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            todos[indice-1] = nueva_tarea
            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        case "completar":
            indice = int(input("Ingrese el número de la lista a completar: "))
            indice -= 1
            todos.pop(indice)
            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        case "salir":
            break
        case _:
            print("No entiendo esta acción")
print("Adióos")
