oracion = input("Ingresa una oración: ")
palabra_antigua = input("Ingresa la palabra a reemplazar: ")
palabra_nueva = input("Ingresa la nueva palabra: ")
nueva_oracion = oracion.replace(palabra_antigua,palabra_nueva)
print(nueva_oracion)