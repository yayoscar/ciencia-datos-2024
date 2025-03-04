nombre_archivo = "texto.txt"
contenido_inicial = input("ingrese una frase: ")
archivo= open(nombre_archivo,"w")
archivo.write(contenido_inicial)
archivo.close()

palabra_buscar = input("Ingresa la palabra que quieres buscar: ")
archivo_lectura = open(nombre_archivo, "r")
contenido_leido = archivo_lectura.read().lower()
archivo_lectura.close()
palabra_buscar = palabra_buscar.lower()
contador = contenido_leido.count(palabra_buscar)

print(f"La palabra '{palabra_buscar}' aparece {contador} veces en el archivo.")