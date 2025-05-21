def promedio_lista(lista):
    if not lista:
        return 0  # Evita división por cero si la lista está vacía
    return sum(lista) / len(lista)

print(promedio_lista([10, 20, 30, 40]))