# informe_funciones.py
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

def imprimir_informe(informe: list) -> None:
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    dash = '-'
    print(f'{dash:->10s} {dash:->10s} {dash:->10s} {dash:->10s}')
    for r in informe:
        print('%10s %10d $%9.2f $%9.2f' % r)

def informe_camion(csv_camion: str, csv_precios: str) -> None:
    imprimir_informe(hacer_informe(leer_camion(csv_camion), leer_precios(csv_precios)))

informe_camion('../Data/camion.csv', '../Data/precios.csv')
