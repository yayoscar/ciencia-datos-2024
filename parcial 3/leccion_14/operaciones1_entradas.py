from operaciones import *

def main():
 # Suma
 print("Suma:")
 print(f"2 + 3 = {sumar(2, 3)}")
 print(f"5 + 1 = {sumar(5, 1)}")

 # Resta
 print("\nResta:")
 print(f"5 - 2 = {restar(5, 2)}")
 print(f"8 - 3 = {restar(8, 3)}")

 # Multiplicación
 print("\nMultiplicación:")
 print(f"4 * 5 = {multiplicar(4, 5)}")
 print(f"2 * 9 = {multiplicar(2, 9)}")

 # División
 print("\nDivisión:")
 try:
 print(f"10 / 2 = {dividir(10, 2)}")
 print(f"7 / 0 = {dividir(7, 0)}")
 except ZeroDivisionError as e:
 print(f"Error: {e}")

 main()


