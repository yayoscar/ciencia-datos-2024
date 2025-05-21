# Solicitar una palabra al usuario
palabra = input("Escribe una palabra: ")

# Abrir el archivo y leerlo
archivo = open("texto.txt", "r")
contenido = archivo.read()
archivo.close()

# Contar cuántas veces aparece la palabra
contador = contenido.count(palabra)

# Imprimir el resultado
print(f"La palabra aparece {contador} veces.")