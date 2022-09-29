'''
geringoso.py
Autor: Javier Spina
Ejercicio 1.18, Clase 1
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
2022-08-07
'''

cadena = 'Geringoso'
capadepenapa = ''

vocales = 'aeiouáéíóú'

def geringar(vocal):
    return vocal + 'p' + vocal

for c in cadena:
    if c in vocales:
        capadepenapa += geringar(c)
    else:
        capadepenapa += c

print(f'El geringoso para {cadena} es {capadepenapa}')

'''
stdout:

El geringoso para Geringoso es Geperipingoposopo
'''