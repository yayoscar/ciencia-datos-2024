tareas = []

while True:
    print("\n--- Menú de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        tarea = input("Escribe la tarea que quieres agregar: ")
        tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        if tareas:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas.")

    elif opcion == "3":
        tarea_a_eliminar = input("Escribe el nombre exacto de la tarea a eliminar: ")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("Tarea eliminada.")
        else:
            print("La tarea no se encontró.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
