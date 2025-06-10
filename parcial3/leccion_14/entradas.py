def input_numero(prompt):
     while True:
        try:
            entrada = input(prompt)
            return int(entrada)
        except ValueError:
            print("Dame un numero")


def input_float(prompt):
    while True:
        try:
            entrada = input(prompt)
            return float(entrada)
        except ValueError:
            print("Dame un numero")
