from coche_electrico import CocheElectrico

mi_tesla = CocheElectrico('tesla','model s', 2019)
print(mi_tesla.obtener_nombre_descriptivo())
mi_tesla.bateria.describir_bateria()
#mi_tesla.bateria.obtener_autonomia()
mi_tesla.llenar_tanque_gasolina()