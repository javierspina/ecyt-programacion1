<<<<<<< Updated upstream
=======
#!/usr/bin/env python3
>>>>>>> Stashed changes
# costo_camion.csv
from informe_final import leer_camion

def costo_camion(nombre_archivo: str) -> float:
    '''
    Lee el informe del contentido de un camión y calcula el costo total
    '''
    return sum([item['cajones'] * item['precio'] for item in leer_camion(nombre_archivo)])

# print(costo_camion('Data\camion.csv'))

def f_principal(params: list) -> None:
    print(f'Costo total: {costo_camion(params[1])}')

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
