from coche import Coche
from coche_electrico import CocheElectrico as CE

mi_vocho = Coche('volkswagen', 'beetle', 2019)
print(mi_vocho.obtener_nombre_descriptivo())

mi_tesla = CE('tesla', 'roadster', 2019)
print(mi_tesla.obtener_nombre_descriptivo())