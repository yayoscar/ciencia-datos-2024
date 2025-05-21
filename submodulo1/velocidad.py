def velocidad(ditancia, tiempo):
    dist_km = ditancia
    dist_m=ditancia*1000
    tiempo_S= tiempo*3600
    tiempo_h=tiempo
    vel_kmh=dist_km/tiempo_h
    vel_ms=dist_km/tiempo_S
    resulatdo= "la velocidad  es" + str(vel_kmh) + "km/h" + str(vel_ms) + "m/s"
    return resulatdo
ditancia = 90
tiempo = 1

