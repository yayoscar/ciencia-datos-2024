from os.path import split

with open("temperaturas.txt","r")  as archivo:
    num = archivo.readlines()
    temperatura = []
    temperatura.append(num)
    temperatura = temperatura.split()
    print(temperatura)