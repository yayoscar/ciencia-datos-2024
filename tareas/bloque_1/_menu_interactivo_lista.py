# Lista para almacenar las tareas
tareas = []

while True:
    # Mostrar menú
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea (por nombre)")
    print("4. Salir")

    # Solicitar opción al usuario
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Agregar tarea
        tarea = input("Escribe la nueva tarea: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada.")

    elif opcion == "2":
        # Ver tareas
        if tareas:
            print("\nLista de tareas:")
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas en la lista.")

    elif opcion == "3":
        # Eliminar tarea
        tarea_eliminar = input("Escribe el nombre de la tarea a eliminar: ")
        if tarea_eliminar in tareas:
            tareas.remove(tarea_eliminar)
            print(f"Tarea '{tarea_eliminar}' eliminada.")
        else:
            print(f"Tarea '{tarea_eliminar}' no encontrada.")

    elif opcion == "4":
        # Salir del programa
        print("Saliendo del programa. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
