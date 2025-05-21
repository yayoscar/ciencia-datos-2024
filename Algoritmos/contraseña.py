contraseña = input("introduce contraseña: ")

contiene_mayuscula = any(c.isupper() for c in contraseña)
contiene_minusculas = any(c.islower() for c in contraseña)
contiene_numero = any(c.isdigit() for c in contraseña)

print("\resultados de validacion:")
print("contiene mayusculas:", "si" if contiene_mayuscula else "no")
print("contiene minusculas", "si" if contiene_minusculas else "no")
print("contiene numeros:", "si" if contiene_numero else "no")

if contiene_mayuscula and contiene_minusculas and contiene_numero:
 print("la contraseña es valida.")
else:

 print("la contraseña no cumple con todo.")


