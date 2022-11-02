<<<<<<< Updated upstream
=======
#!/usr/bin/env python3
>>>>>>> Stashed changes
# informe_final.py
from fileparse import parse_csv

def leer_camion(nombre_archivo: str) -> list:
    '''
    Lee un archivo que contiene los costos de frutas y verduras y los devuelve en una lista de diccionarios.
    '''
    return parse_csv(nombre_archivo, types=[str, int, float])

def leer_precios(nombre_archivo: str) -> dict:
    '''
    Lee un archivo que contiene los precios de venta y devuelve un diccionario de forma Nombre: Precio.
    '''
    return dict(parse_csv(nombre_archivo, types=[str, float], has_headers=False))

def hacer_informe(camion: list, precios: list) -> list:
    '''
    Crea una lista de tuplas que contiene los productos vendidos y calcula el cambio respecto al costo.
    '''
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
    '''
    Imprime el informe en forma de tabla.
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    dash = '-'
    print(f'{dash:->10s} {dash:->10s} {dash:->10s} {dash:->10s}')
    for r in informe:
        print('%10s %10d $%9.2f $%9.2f' % r)

def informe_camion(csv_camion: str, csv_precios: str) -> None:
    '''
    Imprime el informe respecto de un camion y una lista de precios en particular.
    '''
    imprimir_informe(hacer_informe(leer_camion(csv_camion), leer_precios(csv_precios)))

def f_principal(params: list) -> None:
    informe_camion(params[1], params[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
