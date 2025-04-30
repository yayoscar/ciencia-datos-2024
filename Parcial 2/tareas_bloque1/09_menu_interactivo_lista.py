tareas = []
while True:
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea (por nombre)")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        tarea = input("Escribe la nueva tarea: ")
        tareas.append(tarea)
        print("Tarea agregada.")
    elif opcion == "2":
        if tareas:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas.")
    elif opcion == "3":
        nombre_tarea = input("Escribe el nombre de la tarea a eliminar: ")
        if nombre_tarea in tareas:
            tareas.remove(nombre_tarea)
            print("Tarea eliminada.")
        else:
            print("Tarea no encontrada.")
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")