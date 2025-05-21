pasword=input("password: ")

condiciones = []
largo = False
if len(pasword) >=8:
    condiciones ['largo']=True
else:
    condiciones ['largo']=(False)

digito = False
for letra in password:
    if letra.isdigit():
        digito = True
condiciones['digito']=digito



mayuscula = False
for letra in pasword:
    if letra.isupper():
        mayuscula = True

condiciones['mayuscula']=mayuscula


print(condiciones)
print(condiciones.values())
if all(condiciones.values()):
    print("password Fuerte")
else:
    print("password debil")





