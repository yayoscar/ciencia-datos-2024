oracion = input("Ingresa una oración: ")

palabra_a_reemplazar = input("Ingresa la palabra que deseas reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")

oracion_modificada = oracion.replace(palabra_a_reemplazar, nueva_palabra)

print(f"Oración modificada: {oracion_modificada}")