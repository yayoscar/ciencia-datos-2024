''' CÓDIGO ANTERIOR
archivo = open("datos.txt", 'w')
archivo.write("100.12")
archivo.write("111.23")
archivo.close()
'''
archivo = open("datos.txt", 'w')
archivo.write(f"100.12\n")
archivo.write("111.23")
archivo.close()