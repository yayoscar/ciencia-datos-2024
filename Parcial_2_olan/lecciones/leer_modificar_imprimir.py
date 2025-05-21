ensayo=open(r"C:\Users\omary\Downloads\archivos leccion 6\ensayo.txt",'r',)
contenido= ensayo.read()
ensayo.close()
contenido_modificado= contenido.title()
print(contenido_modificado)


