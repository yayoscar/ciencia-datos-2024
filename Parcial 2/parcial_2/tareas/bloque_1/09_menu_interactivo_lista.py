
def show_menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def main():
    while True:
        show_menu()
        op1 = input("Selecciona una opción: ")

        if op1 == "1":
            op2 = input("Escribe la tarea que deseas agregar: ")
            print(f"Tarea '{op2}' agregada.")

        elif op1 == "2":
            if op2:
                print("\nLista de tareas:")
                for i, task in enumerate(op2, start=1):
                    print(f"{i}. {task}")
            else:
                print("La lista de tareas está vacía.")

        elif op1 == "3":
            if op2:
                print("\nLista de tareas:")
                for i, task in enumerate(op2, start=1):
                    print(f"{i}. {task}")
                try:
                    task_number = int(input("Selecciona el número de la tarea que deseas eliminar: "))
                    if 1 <= task_number <= len(op2):
                        removed_task = op2.pop(task_number - 1)
                        print(f"Tarea '{removed_task}' eliminada.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            else:
                print("La lista de tareas está vacía.")

        elif op1 == "4":
            print("¡Gracias por usar el menú de tareas! Hasta luego.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()