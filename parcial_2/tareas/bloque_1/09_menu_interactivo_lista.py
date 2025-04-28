tareas = []

while True:
    print("\n--- Menú de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea (por nombre)")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        tarea = input("Ingresa el nombre de la tarea: ")
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
        nombre = input("Ingresa el nombre de la tarea a eliminar: ")
        if nombre in tareas:
            tareas.remove(nombre)
            print("Tarea eliminada.")
        else:
            print("Tarea no encontrada.")
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")