oracion = input("Introduce una oración: ")

palabra_a_reemplazar = input("Introduce la palabra que deseas reemplazar: ")
nueva_palabra = input("Introduce la nueva palabra: ")

nueva_oracion = oracion.replace(palabra_a_reemplazar, nueva_palabra)

print(f"La nueva oración es: {nueva_oracion}")
