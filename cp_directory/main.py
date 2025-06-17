def obtener_tareas(ruta_archivo= "todos.txt"):
    """"retorna una lista de taraes a partir de una ruta"""
    with open(ruta_archivo, "r") as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local


def guardar_tareas(todos_arg,ruta_archivo="todos.txt"):
    """"guarda en un archivo la lista de tareas"""
    with open(ruta_archivo, "w") as archivo_local:
        archivo_local.writelines(todos_arg)

        mensaje = "ingrese una tarea: "
todos = []
while True:
    accion_usuario =input("indica que accion desea hacer agregar/mostrar/editar/completar/salir: ")
    accion_usuario=accion_usuario.strip()
    accion_usuario=accion_usuario.lower()

    if  accion_usuario.startswith("agregar") :
       todo = accion_usuario[8:]
       todo = f"{todo}\n"

       todos=obtener_tareas()

       todos.append(todo)

       guardar_tareas(todos)


    elif accion_usuario.startswith("mostrar") :
            todos = obtener_tareas("todos.txt")
            #todos_sin_espacios=[elemento.strip("\n") for elemento in todos]
            for (indice,elemento) in enumerate(todos):
                elemento = elemento.title()
                elemento = elemento.strip("\n")
                print (f"{indice+1}--{elemento}")
    elif accion_usuario.startswith("editar"):
        try:
              indice = int(accion_usuario[7:])
              nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
              nueva_tarea = f"{nueva_tarea}\n"
              todos = obtener_tareas()
              todos[indice-1] = nueva_tarea
              guardar_tareas( todos)
        except  ValueError:
            print("estas ingresando un valor invalido")
            continue
        except IndexError:
            print("el numero esta fuera del rango de tareas")
            continue
    elif accion_usuario.startswith("completar"):
          try:
              indice= int(accion_usuario[10:])
              indice -=1
              todos = obtener_tareas()
              todos.pop(indice)
              guardar_tareas(todos)
          except  ValueError:
              print("estas ingresando un valor invalido")
              continue
          except IndexError:
              print("el numero esta fuera del rango de tareas")
              continue
    elif accion_usuario.startswith("salir") :
            print("nos vemos :(")
            break
    else:
            print("no entiendo esta accion")




#eso tilin wow tilin eso tilin ala mrd tilin


