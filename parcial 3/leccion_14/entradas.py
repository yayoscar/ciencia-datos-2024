def input_int(prompt):
    while True:
        try:
         entrada=input(prompt)
         return int(entrada)
        except ValueError:
            print("debes ingresar un numero")


    def input_float(prompt):
          while True:
             try:
                 entrada = input(prompt)
                 return int(entrada)
             except ValueError:
                 print("debes ingresar un numero")


