tareas = []


def agregar_tarea():
    tarea = input("Ingrese una tarea: ")
    tareas.append(tarea)
    print("Tarea agregada con éxito.")


def ver_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")


def eliminar_tarea():
    tarea = input("Ingrese el nombre de la tarea a eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada con éxito.")
    else:
        print("La tarea no existe.")


while True:
    print("\nMenú de opciones:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")

