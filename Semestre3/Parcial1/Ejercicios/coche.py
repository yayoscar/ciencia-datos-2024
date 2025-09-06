class Coche:
    def __init__(self, marca, modelo, anio):
        """Inicializa atributos para describir un coche."""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.lectura_cuentakilometros=0

    def obtener_nombre_descriptivo(self):
        """Devuelve un nombre descriptivo con buen formato.""" 
        nombre_largo = f"{self.anio} {self.marca} {self.modelo}"
        return nombre_largo.title()
    
    def leer_cuentakilometros(self):
        """Imprime una frase mostrando el kilometraje del coche."""
        print(f"Este coche tiene {self.lectura_cuentakilometros} millas.")
    
    def actualizar_cuentakilometros(self, millaje):
        """Establece la lectura del cuentakilómetros al valor dado."""
        self.lectura_cuentakilometros = millaje
    
    def actualizar_cuentakilometros(self, millaje):
        """
        Establece la lectura del cuentakilómetros al valor dado.
        Rechaza el cambio si intenta hacer retroceder el cuentakilómetros.
        """
        if millaje >= self.lectura_cuentakilometros:
             self.lectura_cuentakilometros = millaje
        else:
             print("¡No puedes hacer retroceder un cuentakilómetros!")
    
    def incrementar_cuentakilometros(self, millas):
        """Suma la cantidad dada a la lectura del cuentakilómetros."""
        self.lectura_cuentakilometros += millas
    
mi_coche_nuevo = Coche('audi', 'a4', 2019)
print(mi_coche_nuevo.obtener_nombre_descriptivo())
mi_coche_nuevo.actualizar_cuentakilometros(23)
mi_coche_nuevo.leer_cuentakilometros()

mi_coche_usado = Coche('subaru', 'outback', 2015)
print(mi_coche_usado.obtener_nombre_descriptivo())
mi_coche_usado.actualizar_cuentakilometros(23_500) 
mi_coche_usado.leer_cuentakilometros()
mi_coche_usado.incrementar_cuentakilometros(100)
mi_coche_usado.leer_cuentakilometros()