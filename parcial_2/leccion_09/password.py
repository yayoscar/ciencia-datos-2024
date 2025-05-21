contraseña = input("ingrese contraseña: ")

condiciones=[]
largo = False
if len(contraseña) >=8:
    condiciones.append(True)
else:
    condiciones.append(False)

mayuscula = False
for letra in contraseña:
    if letra.isdigit():
        digito = True

condiciones.append(digito)


if largo and digito and mayuscula:
    print("contraseña fuerta")
else:
    print("contraseña segura")