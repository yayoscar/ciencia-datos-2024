def contar_vocales(frase):
    frase = frase.lower()


    for i in ["a","e","i","o","u"]:
        print(f"la vocal {i} se repite {frase.count(i)}")

contar_vocales("hola,mundo,python,programacion")

PD = "profe lo tuve que aprender en youtube :D"
print(PD.upper())








