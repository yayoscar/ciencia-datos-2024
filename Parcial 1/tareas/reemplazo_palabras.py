from dataclasses import replace

texto = input("ponga una oracion: ")

while True:
    cambio = input("ingresa la palabra que desees remplazar: ")
    oracion = input("indica la palabra por la cual desees remplazar:  ")
    oracion = (oracion.replace())
    print("oracion modificada: ", oracion)
