def calcular_interes_simple(capital, tasa, tiempo):
  """Calcula el interés simple.

  Args:
    capital: El capital inicial.
    tasa: La tasa de interés anual (en decimal).
    tiempo: El tiempo en años.

  Returns:
    El interés simple ganado.
  """
  interes = capital * tasa * tiempo
  return interes


def calcular_interes_compuesto(capital, tasa, tiempo):

  """
  capital_final = capital
  for _ in range(tiempo):
    capital_final += capital_final * tasa
  interes = capital_final - capital
  return interes


capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (en decimal): "))
tiempo = int(input("Ingrese el tiempo en años: "))

tipo_interes = input("¿Desea calcular el interés simple (s) o el interés compuesto (c)? (s/c): ")

if tipo_interes.lower() == 's':
  interes = calcular_interes_simple(capital, tasa, tiempo)
  print("El interés simple es:", interes)
elif tipo_interes.lower() == 'c':
  interes = calcular_interes_compuesto(capital, tasa, tiempo)
  print("El interés compuesto es:", interes)
else:
  print("Opción no válida. Por favor, ingrese 's' o 'c'.")