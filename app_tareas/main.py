from funciones import funciones_main
from datetime import datetime


fecha = datetime.now()

fecha_str = fecha.strftime('%d/%m/%Y  %H:%M')
print("La fecha actual es", fecha_str)
mensaje = "Ingrese una tarea: "
todos = []
while True:
    accion_usuario = input("Indica que acción quieres realizar agregar/mostrar/editar/completar/salir: ")
    accion_usuario = accion_usuario.lower()
    accion_usuario = accion_usuario.strip()

    if accion_usuario.startswith('agregar'):
        todo = accion_usuario[8:]
        todo = f"{todo}\n"
        todos = funciones_main.leer_tareas()
        todos.append(todo)
        funciones_main.guardar_tareas(todos)
    elif accion_usuario.startswith("mostrar"):
        todos = funciones_main.leer_tareas()
        for indice,elemento in enumerate(todos):
            elemento = elemento.title()
            elemento = elemento.strip('\n')
            print(f"{indice+1}.-{elemento}")
    elif accion_usuario.startswith("salir"):
        break
    elif accion_usuario.startswith("editar"):
        try:
            indice = int(accion_usuario[7:])
            nueva_tarea = input("Ingrese el nuevo valor para la tarea: ")
            nueva_tarea = f"{nueva_tarea}\n"
            todos = funciones_main.leer_tareas()
            todos[indice-1] = nueva_tarea
            funciones_main.guardar_tareas(todos)
        except ValueError:
            print("Estás ingresando un valor no válido")
            continue #resetea el ciclo
        except IndexError:
            print("El número está fuera del rango del total de tareas")
            continue
    elif accion_usuario.startswith("completar"):
        try:
            indice = int(accion_usuario[10:])
            indice -= 1
            todos = funciones_main.leer_tareas()
            todos.pop(indice)
            funciones_main.guardar_tareas(todos)
        except ValueError:
            print("Estás ingresando un valor no válido")
            continue
        except IndexError:
            print("El número está fuera del rango del total de tareas")
            continue
    else:
        print("No entiendo esta acción.")
print("Adiós")