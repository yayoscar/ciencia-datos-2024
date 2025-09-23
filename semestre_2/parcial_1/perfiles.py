from usuario import Usuario
from admin import Admin

us1 = Usuario('Tito', 'Capotito', 'tito.capotito@cbtis72.edu.mx', '1111')
us2 = Usuario('Tralalero', 'Tralalá', 'tralalero@gmail.com', '1234')
us3 = Usuario('Lin Manuel', 'Miranda', 'lmm@gmail.com', '49352')
us1.describir_usuario()
us1.saludar_usuario()

us2.describir_usuario()
us2.saludar_usuario()

us3.describir_usuario()
us3.saludar_usuario()

us4 = Usuario("Yana", "Cruz", "lolita", "1234")
us4.saludar_usuario()
us4.incrementar_intentos_inicio_sesion()
print(us4.intentos_inicio_sesion)
us4.incrementar_intentos_inicio_sesion()
print(us4.intentos_inicio_sesion)
us4.incrementar_intentos_inicio_sesion()
print(us4.intentos_inicio_sesion)
us4.reiniciar_intentos_inicio_sesion()
print(us4.intentos_inicio_sesion)

admin = Admin("Yana", "Balam", "yana.balam", 1234)
admin.saludar_usuario()
admin.privilegios.mostrar_privilegios()

admin = Admin("Hugo", "Balam", "hugo.balam", 1083)
admin.saludar_usuario()
admin.privilegios.mostrar_privilegios()