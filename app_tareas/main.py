mensaje = "ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("indica que quieres realizar agregar/mostrar/editar/salir:  " )
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith("agregar"):
        todo = accion_usuario[8:]
        todo = f"{todo}\n"

        with open("todos.txt", "r") as archivo:
            todos = archivo.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as archivo:
            archivo.writelines(todos)


    elif accion_usuario.startswith("mostrar"):
        with open("todos.txt", "r") as archivo:
            todos = archivo.readlines()
            print(archivo.read())


        # todos_sin_espacio = [ elemento.strip('\n') for elemento in todos]

        # Aqui eliminamos el salto de linea
        for indice,elemento in enumerate(todos):
            elemento = elemento.title()
            elemento = elemento.strip('\n')
            print(f"{indice+1}--{elemento}")
    elif accion_usuario.startswith("editar"):
        try:
            indice= int(accion_usuario[7:])
            nueva_tarea = input("ingresa el nuevo valor para la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            todos[indice-1] = nueva_tarea
            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        except ValueError:
            print("estas ingresando un valor invalido")
            continue
        except IndexError:
            print("el numero esta fuera del rango de tareas")
            continue
    elif accion_usuario.startswith("completar"):
        try:
            indice= int(accion_usuario[10:])
            indice -= 1
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            todos.pop(indice)
            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        except ValueError:
            print("estas ingresando un valor invalido")
            continue
        except IndexError:
            print("el numero esta fuera del rango total de tareas")
            continue
    elif accion_usuario.startswith("salir"):
        break
    else:
        print("No entiendo esta accion.")
print("Adios")