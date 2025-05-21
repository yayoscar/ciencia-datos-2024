temperatura = float(input("Ingresa la temperatura en grados Celsius: "))

if temperatura <= 0:
    estado = "sólido (hielo)"
elif 0 < temperatura < 100:
    estado = "líquido"
else:
    estado = "gaseoso (vapor)"

print(f"A {temperatura}°C, el agua está en estado {estado}.")
