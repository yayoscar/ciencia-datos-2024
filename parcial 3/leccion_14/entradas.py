def input_numeros(prompt):
    while True:
        try:
             entrada=input(prompt)
             return input(entrada)
        except ValueError:
            print("Debes ingresar un numero")


def input_float(prompt):
    while True:
        try:
            entrada=input()
            return float(entrada)
        except ValueError:
            print("ingrese un numero")

