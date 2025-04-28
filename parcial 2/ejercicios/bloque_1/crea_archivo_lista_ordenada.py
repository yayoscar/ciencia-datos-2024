def crea_archivo_lista_ordenada():
    numeros=[3.5,1.2,4.8,2.1,5.6]
    numeros.sort() 
    with open("orden.txt","w") as archivo:
        archivo.write(",".join(map(str, numeros)))
crea_archivo_lista_ordenada()