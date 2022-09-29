'''
costo_camion.py
Autor: Javier Spina
Ejercicio 2.9, Clase 2
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
Agosto 2022
'''

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
        return f'Costo total: {costo_total}'
        
print(costo_camion('./camion.csv'))

'''
stdout:

Costo total: 47671.15

'''