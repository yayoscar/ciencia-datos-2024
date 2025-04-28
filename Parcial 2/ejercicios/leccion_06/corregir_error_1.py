# Abrir archivo en modo escritura
archivo = open("datos.txt", 'w')

# Escribir valores con salto de línea
archivo.write("100.12\n")
archivo.write("111.23\n")

# Cerrar archivo
archivo.close()