def leer_tareas(ruta_archivo = "todos.txt"):
    with open(ruta_archivo, "r") as archivo_local:
        todos_local = archivo_local.readline()
    return todos_local

def guardar_tareas(todos_arg, ruta_archivo = "todos.txt"):
    with open(ruta_archivo, "w") as archivo_local:
        archivo_local.writelines(todos_arg)


mensaje = "Ingresa una tarea: "
todos = []
while True:
    accion_usuario=input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir: ")
    acccion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.lower()

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
            continue
        except IndexError:
            print("El número esta fuera del rango del total de tareas")
            continue
    elif accion_usuario.startswith("salir"):
        break
    else:
        print("No entiendo esta ación.")
print("Adiós")



