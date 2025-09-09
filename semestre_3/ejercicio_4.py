class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_local = nombre
        self.tipo_comida = tipo
        self.clientes_atendidos = 0

    def mostrar_info(self):
        print(f"Nombre: {self.nombre_local}")
        print(f"Tipo: {self.tipo_comida}")

    def abrir_local(self):
        print(f"{self.nombre_local} está abierto")

    def fijar_clientes(self, num):
        self.clientes_atendidos = num

    def aumentar_clientes(self, num):
        self.clientes_atendidos += num


local = Restaurante("La placita Maya", "Japonesa")
print(f"Clientes atendidos: {local.clientes_atendidos}")
local.mostrar_info()
local.abrir_local()

local.clientes_atendidos = 20
print(f"Clientes atendidos (actualizado): {local.clientes_atendidos}")

local.fijar_clientes(30)
print(f"Clientes atendidos (fijado): {local.clientes_atendidos}")

local.aumentar_clientes(25)
print(f"Clientes atendidos (aumentado): {local.clientes_atendidos}")
