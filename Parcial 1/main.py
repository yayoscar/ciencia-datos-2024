mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()
    match accion_usuario:
        case "agregar"|"añadir":
            todo = input(mensaje)
            todo = f"{todo}\n"
            archivo = open("todos.txt", "r")
            todos = archivo.readlines()
            archivo.close()
            todos.append(todo)
            archivo = open("todos.txt","w")
            archivo.writelines(todos)
            archivo.close()
        case "mostrar"| "listar":
            archivo = open("todos.txt", "r")
            todos = archivo.readlines()
            archivo.close()


            # todos_sin_espacio = [ elemento.strip('\n') for elemento in todos ]

            # Aqui eliminanos el salto de linea
            for indice,elemento in enumerate(todos):
                elemento = elemento.title()
                elemento = elemento.strip('\n')
                print(f"{indice+1}--{elemento}")
        case "editar":
            indice= int(input("Ingrese el número de la lista a editar: "))
            nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            todos[indice-1] = nueva_tarea
            archivo = open("todos.txt", "w")
            archivo.writelines(todos)
            archivo.close()
        case "completar":
            indice = int(input("Ingrese el número de la lista a completar: "))
            indice -= 1
            todos.pop(indice)
            archivo = open("todos.txt", "w")
            archivo.writelines(todos)
            archivo.close()
        case "salir":
            break
        case _:
            print("No entiendo esta acción.")
print("Adiós")