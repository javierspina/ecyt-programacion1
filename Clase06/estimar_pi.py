'''
estimar_pi.py
Autor: Javier Spina
Septiembre 2022
'''
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x, y

def pi_aproximado(N):
    M = 0
    for i in range(N):
        x, y = generar_punto()
        if x**2 + y**2 < 1:
            M += 1
    return 4 * M/N

N = 100000
print(f'Con {N} aproximaciones, el valor de Pi es aproximadamente {pi_aproximado(N)}')
