# bbin.py

def donde_insertar(lista:list, x, verbose:bool = False) -> int:
    '''
    Adaptación de búsqueda binaria
    Precondición: la lista está ordenada.
    Devuelve p tal que lista[p] == x, si x está en la lista,
    Devuelve p tal que lista[p-1] < x y lista[p] > x, si x no está en la lista.
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')

    pos = -1
    izq = 0
    der = len(lista) - 1
    no_listado = True

    while izq <= der:
        medio = (izq + der) // 2

        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        
        if lista[medio] == x:
            pos = medio    # ¡elemento encontrado!
            no_listado = False
        if lista[medio] > x:
            der = medio - 1    # descarto mitad derecha
            if no_listado:
                pos = der + 1
        else:    # if lista[medio] < x
            izq = medio + 1    # descarto mitad izquierda
            if no_listado:
                pos = izq - 1
    return pos

donde_insertar([0,2,4,6], 2, verbose=True)