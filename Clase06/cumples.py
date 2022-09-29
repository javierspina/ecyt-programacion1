'''
cumples.py
Autor: Javier Spina
Septiembre 2022
'''

import random

def cumple_mismo_dia(n_personas):
    fechas = random.choices(range(1, 366), k = n_personas)
    for f in set(fechas):
        fechas.remove(f)
    return fechas

N = 10000
personas = 13
R = sum([bool(cumple_mismo_dia(personas)) for i in range(N)])

print(f'De {N} estudios, {R} terminaron con al menos 2 personas en un grupo de {personas} cumpliendo el mismo día.')
print(f'Podemos estimar la probabilidad de repetir un cumpleaños en un grupo de {personas} en {R/N:.6f}.')
