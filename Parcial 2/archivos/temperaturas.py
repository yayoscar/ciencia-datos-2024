
def obtener_temperatura():
    with (open("archivos/data.txt","r") as archivo) :
        data = archivo.readlines()
    return

temperatura = obtener_temperatura()
print(temperatura)