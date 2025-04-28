with open("texto.txt", "r") as archivo:
  texto = archivo.read()
palabra = input("Ingresa una palabra: ")
apariciones = texto.count(palabra)
print(f"La palabra '{palabra}' aparece {apariciones} veces.")