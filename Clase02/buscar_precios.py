'''
buscar_precios.py
Autor: Javier Spina
Ejercicio 2.7, Clase 2
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
Agosto 2022
'''

def buscar_precio(producto):
    filepath = './precios.csv'
    
    failed = f'{producto} no figura en el listado de precios.'
    success = ''
    with open(filepath, 'rt') as src:
        headers = next(src)
        price = 0.0
        for line in src:
            unit = line.split(',')
            if unit[0] == producto:
                price = unit[1]
        success = f'El precio de un cajón de {producto} es: {price}'
    
    if price:
        print(success, end='')
    else:
        print(failed)

'''
stdout:

buscar_precio('Lechuga')
El precio de un cajón de Lechuga es: 24.22

buscar_precio('Sandia')
Sandia no figura en el listado de precios.
'''