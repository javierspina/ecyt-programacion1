# informe_final.py
from fileparse import parse_csv
import lote
import formato_tabla


def leer_camion(nombre_archivo: str) -> list:
    """
    Lee un archivo que contiene los costos de frutas y verduras.
    Los devuelve en una lista de diccionarios.
    """
    return parse_csv(nombre_archivo, types=[str, int, float])


def leer_precios(nombre_archivo: str) -> dict:
    """
    Lee un archivo que contiene los precios de venta.
    Devuelve un diccionario de forma Nombre: Precio.
    """
    csv = parse_csv(nombre_archivo, types=[str, float], has_headers=False)
    return dict(csv)


def hacer_informe(camion: list, precios: list) -> list:
    """
    Crea una lista de tuplas que contiene los productos vendidos.
    Calcula el cambio respecto al costo.
    """
    informe = []
    for record in camion:
        nombre = record['nombre']
        if nombre in precios:
            n_cajones = int(record['cajones'])
            precio = float(record['precio'])
            producto = lote.Lote(nombre, n_cajones, precio)
            cambio = float(precios[nombre]) - producto.precio
            info = (producto.nombre, producto.cajones, producto.precio, cambio)
            informe.append(info)
    return informe


def imprimir_informe(data_informe, formateador):
    """
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    """
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt='txt'):
    """
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    """
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    data_informe = hacer_informe(camion, precios)

    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


def f_principal(params: list) -> None:
    if len(params) == 4:
        informe_camion(params[1], params[2], params[3])
    else:
        informe_camion(params[1], params[2])


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
