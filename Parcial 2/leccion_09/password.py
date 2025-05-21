password = input("Password: ")

condiciones=[]
largo = False
if len(password) >= 8:
    condiciones.append(True)
else:
    condiciones.append(False)

digito=False
for letra in password:
    if letra.isdigit():
        digito = True

condiciones.append(digito)

mayuscula = False
for letra in password:
    if letra.isupper():
        mayuscula=True

if all(condiciones):
    print("Password Fuerte")
else:
    print("Password debil")