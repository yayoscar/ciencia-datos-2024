def input_int(prompt):
    while True:
        try:
            entrada = int(input(prompt))
            return entrada
        except ValueError:
            print("Debes ingresar un número")


def input_float(prompt):
    while True:
        try:
            entrada = float(input(prompt))
            return entrada
        except ValueError:
            print("Debes ingresar un número")