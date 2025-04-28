tareas = []

while True:
    print("\n1. Agregar tarea\n2. Ver tareas\n3. Eliminar tarea\n4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        print("\nTareas:")
        i = 0
        while i < len(tareas):
            print(f"{i+1}. {tareas[i]}")
            i += 1
    elif opcion == "3":
        nombre = input("Escribe el nombre de la tarea a eliminar: ")
        if nombre in tareas:
            tareas.remove(nombre)
        else:
            print("Tarea no encontrada.")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
