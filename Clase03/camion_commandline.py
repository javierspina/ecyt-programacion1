'''
costo_commandline.py
Autor: Javier Spina
Ejercicio 3.11, Clase 3
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
Agosto 2022
'''

import sys
import csv

def costo(item, cantidad, precio):
    try:
        calc = int(cantidad) * float(precio)
        return round(calc, ndigits=2)
    except ValueError:
        print(f'Error calculando costo para {item}')
        return 0.0
    

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as src:
        units = csv.reader(src)
        headers = next(units)
        costo_total = 0.0
        for u in units:
            costo_u = costo(u[0], u[1], u[2])
            costo_total += costo_u
        return costo_total
        
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

'''
runfile('camion_commandline.py', args='../Data/missing.csv')
Error calculando costo para Mandarina
Error calculando costo para Naranja
Costo total: 30381.15

runfile('camion_commandline.py')
Costo total: 47671.15
'''