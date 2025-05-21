def leer_tareas():
    """Retorna una lista de tareas a partir de una ruta."""
    with open("todos.txt", "r") as archivo_local:
        todos_local = archivo_local.readline()
    return todos_local

def guardar_tareas(todos_arg,ruta_archivo="todos.txt"):
    with open(ruta_archivo,"w") as archivo_local:
        archivo_local.writelines(todos_arg)


mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith("agregar"):
        todo = accion_usuario[8:]
        todo = f"{todo}\n"

        todos = leer_tareas()

        todos.append(todo)

        guardar_tareas(todos)



    elif accion_usuario.startswith("mostrar"):
        todos = leer_tareas()




        for indice, elemento in enumerate(todos):
            elemento = elemento.title()
            elemento = elemento.strip('\n')
            print(f"{indice+1}--{elemento}")
    elif accion_usuario.startswith("editar"):
        try:
            indice = int(accion_usuario[7:])
            nueva_tarea = input("Ingrese el nuevo valor de la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            todos[indice-1] = nueva_tarea
            with open ("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        except ValueError:
            print("Estás ingresando un valor inválido. ")
            continue
        except IndexError:
            print("El número está fuera del rango de tareas. ")
            continue
    elif accion_usuario.startswith("completar"):
        try:
            indice = int(accion_usuario[10:])
            indice -= 1
            with open("todos.txt", "r") as archivo:
                todos = archivo.readlines()
            todos.pop(indice)
            with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
        except ValueError:
            print("Estás ingresando un valor inválido. ")
            continue
        except IndexError:
            print("El número está fuera del rango total de tareas. ")
            continue
    elif accion_usuario.startswith("salir"):
        break
    else:
        print("No entiendo esta acción.")
print("Adiós.")


