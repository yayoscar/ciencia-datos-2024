def temperaturas_promedio():
    with open("temperatura.txt", "r") as archivo_local:
        todos_local = archivo_local.readlines()
        temperatura = [float(tem) for tem in todos_local]
    return round(sum(temperatura) / len(temperatura), 2)

print(temperaturas_promedio())

def temperaturas_max_min():
    with open("temperatura.txt", "r") as archivo_local:
        todos_local = archivo_local.readlines()
        temperatura = [float(tem) for tem in todos_local]
    return max(temperatura), min(temperatura)

print(temperaturas_max_min())

def temperaturas_mayuscula():
    with open("temperatura.txt", "r") as archivo_local:
        todos_local = archivo_local.readlines()
        temperatura = [float(tem) for tem in todos_local]
    return temperatura

print(temperaturas_mayuscula())




