# fileparse.py
import csv

def parse_csv(nombre_archivo: str, seleccion:list = None, tipos:list = None, tiene_encabezados:bool = True) -> list:
    '''
    Parsea un archivo .csv en una lista de registros
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede indicar los tipos de datos en las columnas para castear los datos
    '''

    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if tiene_encabezados:
            encabezados = next(filas)

        # Si se indicó un selector de columnas, buscar los índices de las columnas especificadas. En ese caso, achicar el conjunto de encabezados para diccionarios.
        if seleccion:
            indices = [encabezados.index(nombre_columna) for nombre_columna in seleccion]
            encabezados = seleccion
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas sin datos
                continue

            # Filtrar la fila si se espeficaron columnas
            if indices:
                fila = [fila[indice] for indice in indices]

            # Casteo del tipo de datos
            if tipos:
                fila = [func(val) for func, val in zip(tipos, fila)]

            # Armado del diccionario o tupla
            if tiene_encabezados:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)
            registros.append(registro)

    return registros

precios = parse_csv('/Users/javierspina/Documents/jspina/ecyt-programacion1/Data/precios.csv', tipos=[str, float], tiene_encabezados=False)