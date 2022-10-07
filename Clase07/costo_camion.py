# costo_camion.csv
from informe_funciones import leer_camion
    
def costo_camion(nombre_archivo: str) -> float:
    '''
    Lee el informe del contentido de un camión y calcula el costo total
    '''
    return sum([item['cajones'] * item['precio'] for item in leer_camion(nombre_archivo)])

costo_camion('/Users/javierspina/Documents/jspina/ecyt-programacion1/Data/camion.csv')
