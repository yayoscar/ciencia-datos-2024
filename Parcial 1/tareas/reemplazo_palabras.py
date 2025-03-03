# Solicita una oración al usuario
oracion = input("Ingrese una oración: ")

# Pide una palabra para reemplazar y una nueva palabra
palabra_vieja = input("Ingrese la palabra a reemplazar: ")
palabra_nueva = input("Ingrese la nueva palabra: ")

# Usa replace() para modificar el texto
nueva_oracion = oracion.replace(palabra_vieja, palabra_nueva)

# Muestra la nueva oración
print("La nueva oración es:", nueva_oracion)