tareas = []

while True:
    print("\n1. Agregar tarea\n2. Ver tareas\n3. Eliminar tarea\n4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        print("Tareas:", tareas)
    elif opcion == "3":
        tarea = input("Tarea a eliminar: ")
        if tarea in tareas:
            tareas.remove(tarea)
        else:
            print("Tarea no encontrada.")
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
