palabras = ["hola", "mundo", "python", "programacion"]
vocales= "a,e,i,o,u"
for palabra in palabras:
    contador=sum(palabra.count(vocales)for vocales in vocales)
    print(contador)