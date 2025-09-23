from coche import Coche

mi_coche_nuevo = Coche('Toyota', "Taigun", 2025)
print(mi_coche_nuevo.obtener_nombre_descriptivo())
mi_coche_nuevo.lectura_cuentakilómetros=23
mi_coche_nuevo.leer_cuentakilómetros()
mi_coche_nuevo.actualizar_cuentakilómetros(24)
mi_coche_nuevo.leer_cuentakilómetros()

mi_coche_usado = Coche('subaru', 'outback', 2015)
print(mi_coche_usado.obtener_nombre_descriptivo())
mi_coche_usado.actualizar_cuentakilómetros(23500)
mi_coche_usado.leer_cuentakilómetros()
mi_coche_usado.incrementar_cuentakilómetros(100)
mi_coche_usado.leer_cuentakilómetros()