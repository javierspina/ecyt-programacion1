'''
costo_camion.py
Autor: Javier Spina
Agosto 2022
ECyT UNSAM - Programación 1
'''

import csv
    
def costo_camion(nombre_archivo):
    costo_total = 0.0
    with open(nombre_archivo, 'rt') as src:
        rows = csv.reader(src)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                costo_producto = int(record['cajones']) * float(record['precio'])
                costo_total += costo_producto
            except ValueError:
                print(f'Fila {i}: No pude interpretar: {row}')
    return costo_total

'''
$ costo_camion('../Data/missing.csv')
stdout:
    Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
    Fila 7: No pude interpretar: ['Naranja', '', '70.44']
'''