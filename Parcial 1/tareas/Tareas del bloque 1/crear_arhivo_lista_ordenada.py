def ordenar_y_guardar():
    # Crear una lista con al menos 5 números flotantes desordenados
    numeros = [3.14, 1.618, 9.81, 2.71, 0.577]

    # Ordenar la lista
    numeros_ordenados = sorted(numeros)

    # Convertir la lista a una cadena separada por comas
    contenido = ", ".join(str(num) for num in numeros_ordenados)

    # Escribir la cadena en el archivo orden.txt
    with open("orden.txt", "w") as archivo:
        archivo.write(contenido)

    print("Números ordenados guardados en 'orden.txt'.")

# Ejecutar función
ordenar_y_guardar()
