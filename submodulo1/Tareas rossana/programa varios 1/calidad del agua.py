temp = float(input("Ingrese la temperatura del agua en grados Celsius: "))

if temp <= 0:
    print("El agua está en estado sólido (hielo).")
elif temp < 100:
    print("El agua está en estado líquido.")
else:
    print("El agua está en estado gaseoso (vapor).")
