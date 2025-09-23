"""Un conjunto de clases usadas para representar coches a gasolina y eléctricos"""

class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.lectura_cuentakilómetros = 0
    def obtener_nombre_descriptivo(self):
        nombre_largo = f"{self.año} {self.marca} {self.modelo}"
        return nombre_largo.title()
    def leer_cuentakilómetros(self):
        print(f"Este coche tiene {self.lectura_cuentakilómetros} kilómetros")
    def actualizar_cuentakilómetros(self, kilometraje):
        if kilometraje >= self.lectura_cuentakilómetros:
            self.lectura_cuentakilómetros = kilometraje
        else:
            print("No puedes hacer retroceder el kilometraje")
    def incrementar_cuentakilómetros(self, kilómetros):
        if kilómetros <0:
            print("No puedes bajarle el kilometraje")
        else:
            self.lectura_cuentakilómetros += kilómetros
