
oracion = input("Por favor, ingresa una oración: ")

palabra_a_reemplazar = input("Ingresa la palabra que deseas reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")

oracion_modificada = oracion.replace(palabra_a_reemplazar, nueva_palabra)

print("La oración modificada es:")
print(oracion_modificada)