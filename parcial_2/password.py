password = input("password: ")
condiciones={}
largo = False
if len(password) >= 8:
    largo = True
condiciones["largo"] = largo
digito = False
for letra in password:
    if letra.isdigit():
        digito = True
condiciones["digito"] = digito
mayus = False
for letra in password:
    if letra.isupper():
        mayus = True
condiciones["mayuscula"] = mayus
print(condiciones)
print(condiciones.values())
if all(condiciones.values()):
    print("contraseña fuerte")
else:
    print("contraseña debil")
