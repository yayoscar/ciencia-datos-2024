RUTA = 'todos.txt'

def leer_tareas(ruta_archivo= RUTA):
    """
    Retorna una variable con la lectura del archivo de ruta
    """
    with open(ruta_archivo, "r") as archivo_local:
        todos_local = archivo_local.readlines()
    return todos_local


def guardar_tareas(todos_arg, ruta_archivo= RUTA):
    with open(ruta_archivo, 'w') as archivo_local:
        archivo_local.writelines(todos_arg)


if __name__ == '__main__':
    print('Hola desde funciones')