password = input("pasword: ")
condiciones=[]
largo= False
if len(password) >=8:
    condiciones.append(True)
else:
    condiciones.append(False)


digito = False
for letra in password:

