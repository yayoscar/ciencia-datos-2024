password = input("Password: ")

condiciones={}
largo = False
if len(password) >=8:
    condiciones['largo']=True
else:
    condiciones['larrgo']=False

digito = False
for letra in password:
    if letra.isdigit():
        digito = True
    condiciones['digito']=digito

mayuscula = False
for letra in password:
    if letra.isupper():
        mayuscula = True

condiciones['mayuscula']=mayuscula

print(condiciones)
print(condiciones.values())
if all(condiciones.values()):
    print("Password fuerte")
else:
    print("Password débil")