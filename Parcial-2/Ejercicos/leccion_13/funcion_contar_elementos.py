def obtener_num_elementos(lista):
    return len(lista)
lista = input("ingrese una lista:  ")
lista = [palabras.strip() for palabras in lista.split(",")]
palabras = obtener_num_elementos(lista)
print(f"la lista tiene {palabras} palabras")