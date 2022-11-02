# fileparse.py
import csv

<<<<<<< Updated upstream
def parse_csv(src, select:list = None, types:list = None, has_headers:bool = True, silence_errors:bool = False) -> list:
    """
=======
def parse_csv(nombre_archivo, select:list = None, types:list = None, has_headers:bool = True, silence_errors:bool = False) -> list:
    '''
>>>>>>> Stashed changes
    Parsea un archivo .csv en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede indicar los tipos de datos en las columnas para castear los datos.
    También con el argumento has_headers se puede indicar si el .csv tiene encabezados o no.
    Para que no se muestren errores en ejecución, seleccionar True para silence_errors.
<<<<<<< Updated upstream
    """
=======
    '''
>>>>>>> Stashed changes

    if select and not has_headers:
        raise RuntimeError('Para seleccionar, necesito encabezados.')

<<<<<<< Updated upstream
    try:
        f = open(src, 'rt')
    except TypeError as e:
        print('[INFO] La entrada no es un archivo.')
        f = src
    finally:
        rows = csv.reader(f)

    if has_headers:
        headers = next(rows)

    if select:
        indexes = [headers.index(column) for column in select]
        headers = select
    else:
        indexes = []

    records = []
    for i, row in enumerate(rows, start=1):
        if not row:
            continue
        if indexes:
            row = [row[indice] for indice in indexes]
        try:
            if types:
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Fila {i}: No pude convertir {row}\nFila {i}: Motivo: {e}')
    
    if f != src:
        f.close()
    return records
=======
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)

        if has_headers:
            headers = next(rows)

        if select:
            indexes = [headers.index(column) for column in select]
            headers = select
        else:
            indexes = []

        records = []
        for i, row in enumerate(rows, start=1):
            if not row:
                continue
            if indexes:
                row = [row[indice] for indice in indexes]
            try:
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i}: No pude convertir {row}\nFila {i}: Motivo: {e}')

    return records

# precios = parse_csv('../Data/precios.csv', types=[str, float], has_headers=False)
>>>>>>> Stashed changes
