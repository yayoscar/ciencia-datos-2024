password = input("password: ")

condiciones=[]
if len(password) >=8:
    print("largo correcto")
else:
    print("largo incorrecto")

mayuscula = False
for letra in password:
    if letra.isupper():
        mayuscula = True

if mayuscula:
    print("cumple con mayuscula")
else:
    print("no cumple con mayuscula")

numero = False
for letra in password:
    if letra.isdigit():
        numero = True

if numero:
    print("si tiene numero")
else:
    print("no tiene numero")


