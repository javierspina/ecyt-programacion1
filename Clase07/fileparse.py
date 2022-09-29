# fileparse.py
import csv

def parse_csv(nombre_archivo: str, select:list = None, types:list = None, has_headers:bool = True) -> list:
    '''
    Parsea un archivo .csv en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede indicar los tipos de datos en las columnas para castear los datos.
    También con el argumento has_headers se puede indicar si el .csv tiene encabezados o no.
    '''

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            headers = next(rows)

        # Si se indicó un selector de columnas, buscar los índices de las columnas especificadas. En ese caso, achicar el conjunto de encabezados para diccionarios.
        if select:
            indexes = [headers.index(column) for column in select]
            headers = select
        else:
            indexes = []

        records = []
        for row in rows:
            if not row:    # Saltear filas sin datos
                continue

            # Filtrar la fila si se espeficaron columnas
            if indexes:
                row = [row[indice] for indice in indexes]

            # Casteo del tipo de datos
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Armado del diccionario o tupla
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

precios = parse_csv('/Users/javierspina/Documents/jspina/ecyt-programacion1/Data/precios.csv', types=[str, float], has_headers=False)