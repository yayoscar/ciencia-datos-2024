def leer_tareas(ruta_archivo="todos.txt"):
    """Retorna una lista de tareas a partir de una ruta"""
    with open(ruta_archivo,"r") as archivo_local :
        todos_local = archivo_local.readlines()
    return todos_local

def guardar_tareas(todos_arg,ruta_archivo="todos.txt"):
    """Guarda en un archivo la lista de tareas"""
    with open(ruta_archivo,"w") as archivo_local:
        archivo_local.writelines(todos_arg)


mensaje = "Ingresa una tarea:"
todos = []
while True:
    accion_usuario = input("Indica que accion quieres realizar agregar/mostrar/editar/completar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith("agregar"):
        todo = accion_usuario[8:]
        todo = f"{todo}\n"

        todos = leer_tareas()

        todos.append(todo)

        with open("todos.txt", "w") as archivo:
                archivo.writelines(todos)
    elif accion_usuario.startswith("mostrar"):
        with open("todos.txt", "r") as archivo:
            todos = archivo.readlines()
            print(archivo.read())

        for indice,elemento in enumerate(todos):
            elemento = elemento.title()
            elemento = elemento.strip('\n')
            print(f"{indice+1}--{elemento}")
    elif accion_usuario.startswith("editar"):
            try:
                indice = int(accion_usuario[7:])
                nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
                nueva_tarea = f"{nueva_tarea}\n"
                todos = leer_tareas()
                todos[indice-1] = nueva_tarea
                guardar_tareas(todos)
            except ValueError:
                print("Estas ingresando un valor inválido")
                continue
            except IndexError:
                print("El número esta fuera del rango del total de tareas")
                continue
    elif accion_usuario.startswith("completar"):
        try:
            indice = int(accion_usuario[10:])
            indice -= 1
            todos = leer_tareas()
            todos.pop(indice)
            guardar_tareas(todos)
        except ValueError:
            print("Estas ingresando un valor inválido")
            continue
        except IndexError:
            print("El número esta fuera del rango del total de tareas")
            continue
    elif accion_usuario.startswith("salir"):
        break
    else:
        print("No entiendo tu mensaje")
print("Adios")