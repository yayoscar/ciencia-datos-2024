def leer_tareas():
    with open("todos.txt", "r") as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local


mensaje = "ingresa una tarea: "
todos = []
while True:
    accion_usuario = input("indica que accion quieres realizar agregar/mostrar/editar/listar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()

    if accion_usuario.startswith("agregar"):
        todo=accion_usuario[8:]
        todo=f"{todo}\n"

        todos=leer_tareas()

        todos.append(todo)

        with open("todos.txt", "r") as archivo:
            todos=archivo.writelines(todos)


    elif accion_usuario.startswith("mostrar"):
        todos=leer_tareas()

        for indice, elemento in enumerate(todos):
            elemento=elemento.title()
            elemento=elemento.strip('\n')
            print(f"{indice+1}--{elemento}")
    elif accion_usuario.startswith("editar"):
        try:
            indice=int(accion_usuario[7:])
            nueva_tarea=input("ingrese le nuevo valor para la tarea: ")
            nueva_tarea= f"{nueva_tarea}\n"
            todos=leer_tareas()
            todos[indice-1]=nueva_tarea
            with open("todos.txt", "w") as archivo:
                todos = archivo.writelines(todos)

        except ValueError:
            print("esta ingresando valor invalido")
            continue
        except IndexError:
            print("el número esta fuera del rango total de tareas")
            continue
    elif accion_usuario.startswith("completar"):
        try:
            indice=int(accion_usuario[10:])
            indice-=1
            todos = leer_tareas()
            todos.pop(indice)
            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        except ValueError:
            print("esta ingresando valor invalido")
            continue
        except IndexError:
            print("el número esta fuera del rango total de tareas")
            continue
    elif accion_usuario.startswith("salir"):
        break
    else:
        print("no entiendo esta accion")
        print("adios")






