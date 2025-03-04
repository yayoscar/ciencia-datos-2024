vocales = "AEIOUaeiou"
palabra = ["hola", "mundo", "phyton", "programacion"]
for palabra in palabra:
    contador = sum(palabra.count(v) for v in vocales)
    print(f' La palabra "{palabra}" tiene {contador} vocales.')



