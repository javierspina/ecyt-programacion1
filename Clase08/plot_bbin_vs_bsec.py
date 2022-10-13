# plot_bbin_bsec.py
import random
import matplotlib.pyplot as plt
import numpy as np

def busqueda_secuencial_comps(lista:list, x) -> tuple:
    '''
    Si x está en la lista devuelve el índice de su primera aparición, de lo contrario devuelve -1.
    Además devuelve la cantidad de comparaciones que hace la función.
    '''
    comps = 0
    pos = -1
    for i,z in enumerate(lista):
        comps += 1
        if z == x:
            pos = i
            break
    return pos, comps

def busqueda_binaria_comps(lista:list, x) -> tuple:
    '''
    La lista debe estar ordenada. Mediante busqueda binaria, si x está en la lista devuelve el índice de su aparición, de lo contrario devuelve -1.
    Además devuelve la cantidad de comparaciones que hace la función.
    '''
    comps = 0
    pos = -1
    izq = 0
    der = len(lista) - 1

    while izq <= der:
        comps += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio
        if lista[medio] > x:
            der = medio - 1
        else:
            izq = medio + 1
    return pos, comps

def generar_lista(n:int, m:int) -> list:
    '''
    Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
    '''
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m:int) -> int:
    '''
    devuelve un elemento aleatorio entre 0 y m
    '''
    return random.randint(0, m-1)

def experimento_secuencial_promedio(lista: list, m: int, k: int) -> float:
    '''
    Devuelve la el promedio de comparaciones que se hicieron en todos los experimentos de busqueda secuencial.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista: list, m: int, k: int) -> float:
    '''
    Devuelve la el promedio de comparaciones que se hicieron en todos los experimentos de busqueda secuencial.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def graficar_bbin_vs_bseq(m: int, k: int, focalizar_graf_binario:bool = False) -> None:
    '''
    Dado el largo de lista experimental m y la cantidad de experimentos k, compara la complejidad de los algoritmos de busqueda secuencial vs binaria.
    si focalizar_graf_binario= True entonces se limita el gráfico en y para mostrar que pasa con la busqueda binaria
    '''
    largos = np.arange(256) + 1
    comps_promedio = (np.zeros(256), np.zeros(256))

    for i, n in enumerate(largos):
        lista = generar_lista(n, m)
        comps_promedio[0][i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio[1][i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos, comps_promedio[0], label = 'Búsqueda Secuencial', color='blue')
    plt.plot(largos, comps_promedio[1], label = 'Búsqueda Binaria', color='red')
    if focalizar_graf_binario:
        plt.ylim(0, int(comps_promedio[1][i]) + 1)
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()

graficar_bbin_vs_bseq(10000, 1000)
graficar_bbin_vs_bseq(10000, 1000, focalizar_graf_binario=True)

# La busqueda binaria tiene una asíntota horizontal, que sería posible de calcular matemáticamente.
