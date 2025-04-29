archivo=open("parrafo","r")
lineas = archivo.readlines()
archivo.close()
print("el archivo tiene",len(lineas),"lineas")