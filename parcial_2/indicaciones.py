#Ejercicio Resumen de temperaturas en una ciudad, objetivo: Escribir un programa qye les lea un archivo con registros de temperatura por hora, calcule un resumen estadistico y genere un reporte,
#Archivo de entrada: temperaturas.txt
#Formato: Cada línea contiene la hora (formato 24h), la temperatura registrada y un nombre de archivo del sensor
#Ejemplo: 08|15.3|sensor_mañana.txt
#12|22.7|sensor_medio.txt
#19|18.4|sensor_noche.txt
#  Lo que debe hacer tu programa: Leer el archivo "temperaturas.txt" usando with
#2Procesar las líneas para: a)obtener el promedio de temperaturas. b)identificar la temperatura maxima y mínima. c)Capitalizar los nombres del archivo sin extensión
#3 Generar un nuevo archivo "reporte_temperaturas.txt" con el siguiente formato:
#Promedio: 18.8
#Máxima:22.7
#Mínima:11.3
#Archivos: Sensor_mañana, Sensor_medio, Sensor_noche
#Funciones sugeridas:
#promedio(lista)
#extraer_nombre_archivo(nombre_archivo)