def input_entero(prompt):
    while True:
        try:
            entrada = input(prompt)
            return int(entrada)
        except ValueError:
            print("debes ingresar un numero")