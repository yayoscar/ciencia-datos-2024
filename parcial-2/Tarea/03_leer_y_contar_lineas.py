archivo=open("parrrafo.txt","r")
lineas = archivo.readlines()
archivo.close()
print("el archivo tiene",len(lineas),"lineas")