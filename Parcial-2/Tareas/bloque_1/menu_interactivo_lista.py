tareas = []

while True:
    print("\n1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        print("Tareas:")
        for tarea in tareas:
            print("-", tarea)
    elif opcion == "3":
        tarea_a_eliminar = input("Escribe el nombre de la tarea a eliminar: ")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("Tarea eliminada.")
        else:
            print("La tarea no existe.")
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opción no valida.")