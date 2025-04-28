def menu_interactivo_lista():
    tareas = []
    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                tarea = input("Ingrese una tarea: ")
                tareas.append(tarea)
            case "2":
                if tareas:
                    print("Tareas:")
                    for i, tarea in enumerate(tareas):
                        print(f"{i+1}. {tarea}")
                else:
                    print("No hay tareas.")
            case "3":
                tarea_eliminar = input("Ingrese el nombre de la tarea a eliminar: ")
                if tarea_eliminar in tareas:
                    tareas.remove(tarea_eliminar)
                    print(f"Tarea '{tarea_eliminar}' eliminada.")
                else:
                    print(f"Tarea '{tarea_eliminar}' no encontrada.")
            case "4":
                break
            case _:
                print("Opción inválida.")

menu_interactivo_lista()