'''
envido.py
Autor: Javier Spina
Septiembre 2022
'''
import random

palos = ['oro', 'copa', 'espada', 'basto']
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

def obtener_mazo():
    return [(valor, palo) for valor in valores for palo in palos]

def obtener_tanto(mano):
    tanto = 0
    conjuntos = {palo: [] for valor, palo in mano}
    for naipe in mano:
        if naipe[0] > 7:
            conjuntos[naipe[1]].append(0)
        else:
            conjuntos[naipe[1]].append(naipe[0])
    for v in conjuntos.values():
        if len(v) == 2:
            tanto = sum(v, 20)
        if len(v) == 3:
            tanto = sum(v[1:], 20)
    return tanto

N = 10000
tanto_buscado = 33
R = sum([bool(obtener_tanto(random.sample(obtener_mazo(), k = 3)) == tanto_buscado) for i in range(N)])

print(f'De {N} veces, hubo {R} envidos con tanto {tanto_buscado}.')
print(f'La probabilidad de sacar {tanto_buscado} de tanto en una mano es {R/N:.6f}')
