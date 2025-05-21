tareas = []

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        if tareas:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas aún.")

    elif opcion == "3":
        tarea_a_eliminar = input("Escribe el nombre exacto de la tarea a eliminar: ")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("Tarea eliminada.")
        else:
            print("Tarea no encontrada.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")