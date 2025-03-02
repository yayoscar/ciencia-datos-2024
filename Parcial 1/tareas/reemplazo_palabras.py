oracion = input("Ingrese una oración: ")
palabra = input("Palabra que desea reemplazar: ")
nueva_palabra = input("Ingresa la nueva palabra: ")

nueva_oracion = oracion.replace(palabra, nueva_palabra)

print("La nueva oración es:", nueva_oracion)
