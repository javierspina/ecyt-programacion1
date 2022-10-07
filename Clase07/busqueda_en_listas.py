# busqueda_en_listas.py

def busqueda_lineal_ordenada(lista:list, e) -> int:
    for i, el in enumerate(lista):
        if el > e:
            return i
    return None

def busqueda_binaria(lista:list, x, verbose:bool = False) -> int:
    '''
    Búsqueda binaria
    Precondición: la lista está ordenada.
    Devuelve -1 si x no está en la lista,
    Devuelve p tal que lista[p] == x, si x está en la lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')

    pos = -1
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2

        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        
        if lista[medio] == x:
            pos = medio    # ¡elemento encontrado!
        if lista[medio] > x:
            der = medio - 1    # descarto mitad derecha
        else:    # if lista[medio] < x
            izq = medio + 1    # descarto mitad izquierda
    return pos