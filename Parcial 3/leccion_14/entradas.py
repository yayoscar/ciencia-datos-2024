def input_numero(prompt):
    while True:
        try:
         entrada=input(prompt)
         return int(entrada)
        except ValueError:
         print("Debes ingresar un numero")