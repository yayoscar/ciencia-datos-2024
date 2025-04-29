def velocidad(distancia, tiempo):
  dist_km=distancia
  dist_m=distancia*1000
  tiempo_s=tiempo*3600
  tiempo_h=tiempo
  vel_kmh=dist_km/tiempo_h
  vel_ms=dist_m/tiempo_s

  resultado="La velocidad es "+str(vel_kmh)+"km/h o "+str(vel_ms)+"m/s"
  return resultado
distancia=90
tiempo=1

print(velocidad(distancia,tiempo))
