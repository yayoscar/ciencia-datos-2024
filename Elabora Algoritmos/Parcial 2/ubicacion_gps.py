lat = 33.499188
lon = 70.615126
lat_domicilio = float(input("Ingrese le latitud de tu domicilio: "))
Lon_domicilio = float(input("Ingresa la longitud de tu domicilio: "))
estoy_al_sur = lat_domicilio - lat > 0
if estoy_al_sur:
    print("Estoy al sur de mi casa")
else:
    print("No estoy al sur de mi casa")