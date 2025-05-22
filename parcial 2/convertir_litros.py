# convertir_litros.py

def litros_a_m3(litros):
    """
    Convierte una cantidad de litros a metros cúbicos.

    Parámetros:
    litros (float): La cantidad en litros a convertir.

    Retorna:
    float: La cantidad equivalente en metros cúbicos.
    """
    metros_cubicos = litros / 1000
    return metros_cubicos


print(litros_a_m3(1500))
