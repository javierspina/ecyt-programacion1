'''
esfera.py
Autor: Javier Spina
Ejercicio 1.13, Clase 1
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
2022-08-07
'''

import math

radio_esfera = float(input("Ingresar el radio de la esfera:\t"))
volumen_esfera = 4 * math.pi * pow(radio_esfera, 3) / 3

print(f"El volumen de la esfera de radio {radio_esfera} es igual a {volumen_esfera}.")

'''
stdout:

Ingresar el radio de la esfera: 6
El volumen de la esfera de radio 6.0 es igual a 904.7786842338604.
'''