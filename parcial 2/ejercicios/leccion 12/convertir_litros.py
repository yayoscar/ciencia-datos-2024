def litros_a_m3 (litros):
   m3=litros/1000
   final=print(f"hay {m3} metros cubicos en {litros} litros")
   return final
litros=int(input("ingrese el numero de litros: "))
print(litros_a_m3(litros))