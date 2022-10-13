# bbin.py

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

def insertar(lista: list, x):
    '''
    Si x pertenece a lista, devuelve la posicion de x en la lista
    Si x no pertenece a la lista, devuelve la posicion donde fue insertado x y ademas lo agrega a la lista
    '''

    pos = donde_insertar(lista, x)
    if x > lista[-1]:
        pos += 1
    if x not in lista:
        lista.insert(pos, x)
    
    return pos
