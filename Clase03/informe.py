'''
informe.py
Autor: Javier Spina
Ejercicio 3.4 - Clase 3
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
Agosto 2022
'''
import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as src:
        rows = csv.reader(src)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        return camion

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print('Error exceptuado.')
        return precios

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')

stock = []
costo_total = 0.0
venta_total = 0.0
for nombre, cajones, precio in camion:
    if nombre in precios:
        costo_producto = cajones * precio
        venta_producto = cajones * precios[nombre]
        producto = (nombre, costo_producto, venta_producto)
        stock.append(producto)
        costo_total += costo_producto
        venta_total += venta_producto

ganancia = round(venta_total - costo_total, ndigits=2)

print(f'Costo: {costo_total}\nVenta: {venta_total}\nGanancia: {ganancia}')

'''
stdout:

Error exceptuado.
Costo: 47671.15
Venta: 62986.1
Ganancia: 15314.95
'''
