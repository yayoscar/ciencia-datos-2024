tareas = []
while True:
    print("\n--- Menú de Tareas ---")
    print("por favor coloque un (1) para agregar tareas")
    print("por favor coloque un (2) para ver las tareas")
    print("por favor coloque un (3) para eliminar tareas")
    print("por favor coloque un (4) para salir ")
    print ()
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        print ()
        tarea = input("Ingrese la nueva tarea: ")
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada")
    elif opcion == '2':
        if not tareas:
            print("Y las tareas donde están??, ni que fuera adivinx para saber que tareas deseas poner ")
        else:
            print("Lista de tareas:")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
    elif opcion == '3':
        if not tareas:
            print("Ayy beba pues nosé donde tu veas tareas para eliminar porque aqui no hay ninguna tarea")
        else:
            nombre_tarea_eliminar = input("Ingrese el nombre de la tarea que desea eliminar: ")
            try:
                tareas.remove(nombre_tarea_eliminar)
                print(f"Tarea '{nombre_tarea_eliminar}' eliminada")
            except ValueError:
                print(f"No se encontró la tarea '{nombre_tarea_eliminar}'.")
    elif opcion == '4':
        print("Adios vv, byeee regresa pronto")
        break