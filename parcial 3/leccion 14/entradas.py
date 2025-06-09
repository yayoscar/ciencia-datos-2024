def int_int(prompt):
    while True:
        try:
            entrada = input(prompt)
            return int(entrada)
        except ValueError:
            print("Debes ingresar un numero")

def int_float(prompt):
    while True:
        try:
            entrada = input(prompt)
            return float(entrada)
        except ValueError:
            print("Debes ingresar un numero")
