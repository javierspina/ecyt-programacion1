# documentacion.py
def valor_absoluto(n):
    """
    Pre: n debe ser un número
    Pos: se devuelve la distancia de n con el elemento neutro de la suma (el cero)
    """
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    """
    Pre: l es una lista de números
    Pos: se devuelve la suma de los elementos pares de la lista l
    """
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    # el invariante es que res contiene la suma de los pares de la lista en cada iteración

def veces(a, b):
    """
    Pre: a y b son números
    Pos: Devuelve 'b' veces sumado el número 'a'
    """
    res = 0
    nb = b
    while nb != 0:
        res += a
        nb -= 1
    return res
    # Invariante res contiene las sumas progresivas de a

def collatz(n):
    """
    Evalua la cantidad de pasos de la Conjetura de Collatz para el n dado.
    Pre: n es un número natural
    Pos: Devuelve la cantidad de pasos que se ejecutan para llegar a 1 según el enunciado en la Conjetura de Collatz
    """
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
    # res contiene la cantidad de pasos que se van ejecutando
