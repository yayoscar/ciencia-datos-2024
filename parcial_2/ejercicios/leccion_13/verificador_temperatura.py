def verificador_temperatura(temp):
    if temp >7:
        return 'Cálido'
    else:
        return 'Frío'


print(verificador_temperatura(8))