def input_entero(prompt):
    while True:
        try:
            entrada = input(prompt)
            return int(entrada)
        except ValueError:
            print("Debes ingresar un número")

def input_float(prompt):
    while True:
        try:
            entrada = input(prompt)
            return float(entrada)
        except ValueError:
            print("Debes ingresar un número")
