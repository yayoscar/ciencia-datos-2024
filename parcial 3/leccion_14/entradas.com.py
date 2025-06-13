def input_numeros(promt):
    while True:
        try:
          entrada=input(promt)
          return int(entrada)
        except ValueError:
            print("Debes ingresar un número")


def input_float(promt):
    while True:
        try:
            entrada = input(promt)
            return float(entrada)
        except ValueError:
            print("Debes ingresar un número")

