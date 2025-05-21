def iva(mercancia):
    iva = (mercancia*0.16)
    return iva
m= float(input("¿cual es el precio de su producto?"))
print("el iva es de:",iva(m))
print("sin iva es de:",m)
print("su costo con iva es:",iva(m)+m)