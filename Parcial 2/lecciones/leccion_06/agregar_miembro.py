archivo=open('miembros.txt','a')
nombre=input('agregar nuevo nombre:')
archivo.write(f'{nombre}\n')
archivo.close()