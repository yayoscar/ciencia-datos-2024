tareas = []

while True:
    print("\nMenú interactivo de Tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        tarea = input("Ingrese una tarea: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada")
    elif opcion == "2":
        if tareas:
            print("\nTareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas")
    elif opcion == "3":
        if tareas:
            tarea_eliminar = input("Ingrese el nombre de la tarea que desea eliminar eliminar: ")
            if tarea_eliminar in tareas:
                tareas.remove(tarea_eliminar)
                print(f"Tarea '{tarea_eliminar}' eliminada")
            else:
                print(f"No se encontró la tarea '{tarea_eliminar}'")
        else:
            print("No hay tareas")
    elif opcion == "4":
        print("Fin del programa")
        break
    else:
        print("Opción inválida, Por favor intente nuevamente")

