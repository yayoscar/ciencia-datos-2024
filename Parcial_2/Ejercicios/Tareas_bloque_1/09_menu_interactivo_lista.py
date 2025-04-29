tareas = []
while True:
    print("\n--- Menu ---")
    print("1. agregar tarea")
    print("2. ver tareas")
    print("3. eliminar tarea(por nombre)")
    print("4. salir")
    opcion = input("ekige una opcion: ")
    if opcion == "1":
        tarea = input("escribe la nueva tarea: ")
        tareas.append(tarea)
        print("tarea agregada")
    elif opcion == "2":
        if tareas:
            print("\nlista tareas: ")
            for i, tarea in enumerate(tareas, start=1):
                print((f"{i}.t{tarea}"))
        else:
            print("no hay tareas")
    elif opcion == "3":
        nombre_tarea = input("escribe el nombre de la tarea a eliminar: ")
        if nombre_tarea in tarea:
            tareas.remove(nombre_tarea)
            print("tarea eliminada")
        else:
            print("tarea no encontrada")
    elif opcion == "4":
        print("!Hasta luego¡")
        break
    else:
        print("Opcion no validao. Intenta de nuevo.")