#Reemplazo_palabras
oracion = input("Ingrese una oración: ")

palabra_reemplazar = input("Ingresa la palabra que deseas reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")
nueva_oracion = oracion.replace(palabra_reemplazar, nueva_palabra)
print("Nueva oración: ", nueva_oracion)