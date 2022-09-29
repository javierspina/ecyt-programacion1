'''
generala.py
Autor: Javier Spina
Septiembre 2022
'''
import random
import numpy as np

def cubilete(dados):
    return np.array([random.randint(1, 6) for i in range(dados)])

def tirar():
    return cubilete(5)

def es_generala(tirada):
    dados_iguales = np.array([tirada == tirada[0]]).sum()
    if dados_iguales != 5:
        return False
    return True

def prob_generala(N):
    G = np.array([es_generala(buscar_generala(minimo_dos_repetidos = True)) for i in range(N)]).sum()
    return G/N

def buscar_generala(minimo_dos_repetidos = True):
    tirada = tirar()
    for turno in range(2):
        freqs = np.array([[(tirada == i).sum(), i] for i in range(1, 7)])
        max_repeticion = freqs[:, 0].max()
        if max_repeticion == 1 and not minimo_dos_repetidos:
            tirada = tirar()
            continue
        max_freq = freqs[freqs[:, 0] == max_repeticion][0]
        tirada = np.array([max_freq[1]] * max_freq[0])
        tirada = np.concatenate((tirada, cubilete(5 - tirada.size)))
    return tirada

N = 100000
P = prob_generala(N)
G = int(P * N)
print(f'De {N} manos, {G} terminaron en generala.')
print(f'Podemos estimar la probabilidad de formar generala mediante {P:.6f}.')
