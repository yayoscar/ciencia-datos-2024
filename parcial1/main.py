
def leer_tareas(ruta_archivo="todos.txt"):
    with open(ruta_archivo, "r") as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local


def guardar_tareas(todos_arg,ruta_archivo="todos.txt"):
    with open(ruta_archivo, "w") as archivo_local:
        archivo_local.writelines(todos_arg)


mensaje= "ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("indica que opcion quieres realizar: agregar/mostrar/editar/completar/salir")
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





        for indice,elemento in enumerate(todos):
            elemento = elemento.title()
            elemento = elemento.strip('\n')
            print(f"{indice+1}--{elemento}")
    elif accion_usuario.startswith("editar"):
        try:
            indice = int(accion_usuario[7:])
            nueva_tarea = input("ingrese el nuevo valor para la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            todos = leer_tareas()
            todos[indice-1] = nueva_tarea
            guardar_tareas(todos)
        except ValueError:
            print("Estas ingresando un valor invalido")
            continue
        except IndexError:
            print("el numero esta afuera del rango total de tareas")
            continue
    elif accion_usuario.startswith("completar"):
        try:
            indice= int(accion_usuario[10:])
            indice -= 1
            todos = leer_tareas()
            todos.pop(indice)
            guardar_tareas(todos)
        except ValueError:
            print("Estas ingresando un valor invalido")
            continue
        except IndexError:
            print("el numero esta afuero del rango total de tareas")
            continue
    elif accion_usuario.startswith("salir"):
        break
    else:
        print("no entiendo esta accion")

print("adios")
