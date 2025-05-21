
tareas = []

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea (por nombre)")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        tarea = input("Escribe la nueva tarea: ")
        tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        if tareas:
            print("\n--- Lista de tareas ---")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas por mostrar.")

    elif opcion == "3":
        tarea_a_eliminar = input("Escribe el nombre exacto de la tarea a eliminar: ")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("Tarea eliminada.")
        else:
            print("La tarea no se encontró en la lista.")

    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
