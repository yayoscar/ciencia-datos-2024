def estado_del_agua(temperatura):
    if temperatura <= 0:
        return "sólido (hielo)"
    elif 0 < temperatura < 100:
        return "líquido (agua)"
    else:
        return "gaseoso (vapor)"

# Entrada del usuario
try:
    temp = float(input("Introduce la temperatura del agua en grados Celsius: "))
    estado = estado_del_agua(temp)
    print(f"A {temp}°C, el agua está en estado {estado}.")
except ValueError:
    print("Por favor, introduce un número válido.")
