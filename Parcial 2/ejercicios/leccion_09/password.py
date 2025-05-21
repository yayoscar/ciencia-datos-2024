password = input("Password: ")

condiciones=[]
largo=False
if len (password) >=8:
    condiciones[largo]=True
else:
    condiciones[largo]=False

digito = False
for letra in password:
    if letra.isdigit():
        digito = True

condiciones[digito]=largo

mayuscula = False
for letra in password:
    if letra.isupper():
        mayuscula = True

 condiciones[mayuscula]=mayuscula



print(condiciones)
print(condiciones.values())
if all(condiciones):
    print("Password Fuerte")
else:
    print("Password Debil")

