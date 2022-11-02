# costo_camion.csv
import lote
from informe_final import leer_camion

def costo_camion(nombre_archivo: str) -> float:
    '''
    Lee el informe del contentido de un camión y calcula el costo total
    '''
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in leer_camion(nombre_archivo)]
    return sum([item.costo() for item in camion])


def f_principal(params: list) -> None:
    print(f'Costo total: {costo_camion(params[1])}')

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
