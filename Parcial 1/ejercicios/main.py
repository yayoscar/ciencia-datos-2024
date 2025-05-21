def leer_tareas():
    with open("todos.txt", "r") as archivo_local:
        todos = archivo.readlines()
        todos_local = archivo_local.readlines()
    return todos_local

mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()
    if "agregar" in accion_usuario:

        if accion_usuario.startswith("agregar")[8:]:
          todo = f"{todo}\n"

        todos = leer_tareas()

        '''archivo = open("todos.txt", "r")
        todos = archivo.readlines()
        archivo.close()'''
        with open("todos.txt", "r") as archivo:
            todos = archivo.readlines()
        todos.append(todo)
        with open('todos.txt', 'w') as archivo:
            archivo.writelines(todos)

    elif accion_usuario.startswith("mostrar"):
        with open("todos.txt", "r") as archivo:
            todos = archivo.readlines()
        '''todos_nuevos = []
                    for item in todos:
                        todos_nuevos.append(item.strip(\n)'''
        for indice,elemento in enumerate(todos):
            elemento = elemento.title()
            elemento = elemento.strip('\n')
            print(f"{indice+1}.-{elemento}")

    elif accion_usuario.startswith("salir"):
        break

    elif accion_usuario.startswith("editar"):
        try:
            indice = int(accion_usuario[7:])
            indice -= 1
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            todos[indice] = nueva_tarea
            with open('todos.txt', 'w') as archivo:
                archivo.writelines(todos)
        except ValueError:
            print("Estás ingresando un valor inválido")
            continue
        except IndexError:
            print("El número está fuera del rango de tareas")
            continue


    elif accion_usuario.startswith("completar"):
        try:
            indice = int(accion_usuario[10:])
            indice -= 1
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            todos.pop(indice)
            archivo = open("todos.txt", "w")
            archivo.writelines(todos)
            archivo.close()
        except ValueError:
            print("Estás ingresando un valor inválido")
            continue
        except IndexError:
            print("El número está fuera del rango de tareas")
            continue


    else:
        print("No entiendo esta acción.")
print("Adiós")