nuevo_miembro = input("Ingrese el nombre del nuevo miembro: ")

with open('miembros.txt', 'a', encoding='utf-8') as archivo:
    archivo.write(nuevo_miembro + '\n')

print("Contenido actualizado del archivo:")
with open('miembros.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        print(linea, end='')
