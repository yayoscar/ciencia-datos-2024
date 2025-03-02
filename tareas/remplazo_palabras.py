oracion = input("Ingresa una oración: ")
palabra_reemplazar = input("Ingresa la palabra que quieres reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")


oracion_modificada = oracion.replace(palabra_reemplazar, nueva_palabra)


print("La oración modificada es: ", oracion_modificada)