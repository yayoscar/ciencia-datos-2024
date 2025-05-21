'''dict_calificaciones = {
    'español': 7,
    'mate': 8,
    'programación': 10,
    'física': 7,
    'ética': 5
}
print(dict_calificaciones)
print(dict_calificaciones['física'])
print(dict_calificaciones.get('matemáticas', "No especificado"))
print(dict_calificaciones.get('mate', "No especificado"))
dict_calificaciones['inglés'] = 9
print(dict_calificaciones)
dict_calificaciones['inglés'] = 10
print(dict_calificaciones)
reprobado = dict_calificaciones.pop('ética')
print(reprobado)
print(dict_calificaciones)
#del dict_calificaciones['ética']
print(dict_calificaciones)
for llave, valor in dict_calificaciones.items():
    print(f"{llave}:{valor}")'''
lista = ['aunqur', 'bee', 'cool', 'day']
cadena = "CADENA0081ÑÑÑnnnnnn"
entero = 8
flotante = 8.1
print(cadena, cadena.count('a'))
frase = "Esta es una frase"
palabras = frase.split()
print(palabras)
print(lista)
lista.clear()
print(lista)
print(cadena.swapcase(), cadena.casefold(), cadena.isascii())
if flotante.is_integer():
    print('sí',int(flotante))
else:
    print('no', flotante)
