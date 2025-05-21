print("ingresa el ph que saco un idicador de ph o algo parecido antes de responder las preguntas")
acidez = int(input(("Cual es el ph de la tierra donde cultivaste la naranja??")))

if acidez >=2 and acidez<4:
    print("Tienes naranja agria")
elif acidez ==4:
    print("Sigues teniendo naranja agria")
elif acidez >=5 and acidez<7:
    print("tienes naranja dulce en tu terreno que puede acercarse a ser naranja agria pero seria por otras propiedades quimicas ")
elif acidez == 7:
    print("sigues teniendo naranja dulce aunque no es muy comun,checa el medidor del ph")
elif acidez >7 and acidez<9:
    print("checa de nuevo el ph,ya que no es comun en una naranja,una naranja que ha superdo ese ph deja de ser acido y se vuelve alcalino")
else :
    print("Error")