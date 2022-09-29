'''
tabla_informe.py
Autor: Javier Spina
Agosto 2022
ECyT UNSAM - Programación 1
'''

import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as src:
        rows = csv.reader(src)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            camion.append(record)
    return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as src:
        rows = csv.reader(src)
        for i, row in enumerate(rows, start=1):
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'Fila {i}: No pude leer {row}')
    return precios

def hacer_informe(camion, precios):
    informe = []
    for record in camion:
        nombre = record['nombre']
        if nombre in precios:
            precio = float(record['precio'])
            cajones = int(record['cajones'])
            cambio = float(precios[nombre]) - precio
            info = (nombre, cajones, precio, cambio)
            informe.append(info)
    return informe

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('%10s %10s %10s %10s' % headers)
dash = '-'
print(f'{dash:->10s} {dash:->10s} {dash:->10s} {dash:->10s}')
for r in informe:
    print('%10s %10d $%9.2f %10.2f' % r)
    
'''
stdout:
    
    Fila 31: No pude leer []
        Nombre    Cajones     Precio     Cambio
    ---------- ---------- ---------- ----------
          Lima        100 $    32.20       8.02
       Naranja         50 $    91.10      15.18
         Caqui        150 $   103.44       2.02
     Mandarina        200 $    51.23      29.66
       Durazno         95 $    40.37      33.11
     Mandarina         50 $    65.10      15.79
       Naranja        100 $    70.44      35.84
'''