

def calcular_interes_simple(c, ts, t):

    interes = c * (ts / 100) * t
    return interes

def calcular_interes_compuesto(c, ts, t):
    monto = c
    for i in range(t):
        monto += monto * (ts / 100)
    return monto
