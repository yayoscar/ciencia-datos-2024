promedio = float(input("Ingresa tu promedio: "))
es_atleta = input("Eres atleta? ")
positivo = "Aplicas a la beca"
negativo = "No aplicas a la beca"
if es_atleta == "no":
    es_atleta = False
else:
    es_atleta = True
if promedio >= 8.5 or es_atleta == True:
    print(positivo)
else:
    print(negativo)