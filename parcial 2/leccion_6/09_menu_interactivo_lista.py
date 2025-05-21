tareas = []

while True:
    print("\n1. Agregar tarea")
    print("2. ver tareas")
    print("3. eliminar tarea")
    print("4. salir")
    opcion = input("selecciona una opcion: ")

    if opcion == "1":
        tarea = input("escribe la tarea:")
        tareas.append(tarea)
    elif opcion == "2":
        print("tareas:")
        for tarea in tareas:
            print("-", tarea)
    elif opcion == "3":
        tarea_a_eliminar = input("Escribe el nombre de la tarea a eliminar:")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("tarea eliminada.")
        else:
            print("la tarea no existe.")
    elif opcion == "4":
        print("hasta luego")
        break
    else:
        print("opcion no valida")
