from usuario_modulo import Usuario
from admin_modulo import Admin

admin_multi = Admin("Multi", "Modulo", ["priv1", "priv2"])
admin_multi.privilegios.mostrar_privilegios()
