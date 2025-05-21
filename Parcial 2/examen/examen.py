def promedio_de_temperaturas(promedio_temp):
    temperaturas = [float(temperatura) for temperatura in promedio_temp.split(',')]
    return round(sum(temperaturas) / len(temperaturas), 2)

def identificar_temperaturas(a,b):
    return max(a),min(b)

with open('temperaturas.txt','r') as archivo:
    lineas =   archivo.readline()

with open("reporte_temperaturas.txt", "w") as salida:
        for linea in lineas:


          promedio, tem = lineas.strip().split('|')
          promedios = promedio_de_temperaturas(promedio)
          temp = identificar_temperaturas(max,min)
          salida.write(f"promedio de temperaturas: {promedio} - temperaturas: {max,min}-")
