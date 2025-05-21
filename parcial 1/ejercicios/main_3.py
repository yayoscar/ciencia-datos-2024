mensaje = "Ingresa una tarea: "
todos = []

while True:
    accion_usuario = input("Indica qué acción quieres realizar (agregar/mostrar/editar/completar/salir): ").strip().lower()

    match accion_usuario:
        case "agregar" | "añadir":
            todo = input(mensaje) + "\n"
            with open("todos.txt", "a") as archivo:
                archivo.write(todo)

        case "mostrar" | "listar":
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            for indice, elemento in enumerate(todos):
                print(f"{indice + 1} -- {elemento.strip().title()}")

        case "editar":
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()

            try:
                indice = int(input("Ingrese el número de la tarea a editar: "))
                nueva_tarea = input("Ingrese el nuevo valor para la tarea: ") + "\n"
                todos[indice - 1] = nueva_tarea
                with open("todos.txt", "w") as archivo:
                    archivo.writelines(todos)
            except (ValueError, IndexError):
                print("Índice inválido.")

        case "completar":
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()

            try:
                indice = int(input("Ingrese el número de la tarea completada: "))
                todos.pop(indice - 1)
                with open("todos.txt", "w") as archivo:
                    archivo.writelines(todos)
            except (ValueError, IndexError):
                print("Índice inválido.")

        case "salir":
            print("Adiós")
            break

        case _:
            print("No entiendo esta acción.")
