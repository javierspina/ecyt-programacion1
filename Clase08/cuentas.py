def sumar_enteros_loop(desde:int, hasta:int) -> int:
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    assert type(desde) == type(hasta) == int, 'Se esperan números enteros.'
    if hasta <= desde:
        return 0
    sumatoria = 0
    for i in range(desde, hasta+1):
        sumatoria += i
    return sumatoria


def numero_triangular(n):
    return n * (n-1) // 2

def sumar_enteros(desde:int, hasta:int) -> int:
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    assert type(desde) == type(hasta) == int, 'Se esperan números enteros.'
    if hasta <= desde:
        return 0
    return numero_triangular(desde) - numero_triangular(hasta)