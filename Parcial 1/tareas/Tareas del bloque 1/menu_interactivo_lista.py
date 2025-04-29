def mostrar_menu():
    print("Menú de Tareas:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea(tareas):
    tarea = input("Ingresa la tarea que deseas agregar: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def ver_tareas(tareas):
    if tareas:
        print("Tareas actuales:")
        for tarea in tareas:
            print(f"- {tarea}")
    else:
        print("No hay tareas en la lista.")

def eliminar_tarea(tareas):
    tarea = input("Ingresa el nombre de la tarea que deseas eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada.")
    else:
        print("Tarea no encontrada.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
main()
