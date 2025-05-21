tareas = []

while True:
    print("Menú:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        if tareas:
            print("Tareas actuales:")
            for tarea in tareas:
                print(tarea)
        else:
            print("No hay tareas.")
    elif opcion == "3":
        tarea = input("Ingresa el nombre de la tarea a eliminar: ")
        if tarea in tareas:
            tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print("Tarea no encontrada.")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")