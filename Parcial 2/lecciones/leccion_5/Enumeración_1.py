# 1. Itere sobre los elementos de la lista,
# 2. Imprima el índice de cada elemento, seguido de dos puntos “:” y el elemento.


productos = ['mesa', 'silla', 'puerta']
for i,producto in enumerate(productos):
    print(f'{i} : {producto}')
