#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:56:21 2022

@author: javier
"""
import random

def tirar():
    return [random.randint(1, 6) for i in range(5)]

def es_generala(tirada):
    valor_dado = None
    for dado in tirada:
        if not valor_dado:
            valor_dado = dado
            continue
        if valor_dado != dado:
            return False
    return True

N = 100000

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
