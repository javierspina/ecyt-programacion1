#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:15:11 2022

@author: Javier Spina
"""

def buscar_u_elemento(lista, elemento):
    pos = -1
    for i, elemento_lista in enumerate(lista):
        if elemento == elemento_lista:
            pos = i
    return pos

def buscar_n_elemento(lista, elemento):
    cantidad = 0
    for elemento_lista in lista:
        if elemento == elemento_lista:
            cantidad += 1
    return cantidad

def maximo(lista):
    '''Devuelve el máximo de una lista, la lista debe ser no vacía y de números positivos.'''
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = lista[0] # Lo inicializo en el primer valor de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m: # es e mayor que m?
            m = e # entonces actualizar m con el valor de e
    return m

def minimo(lista):
    n = len(lista)
    minimo = lista[n-1]
    while n > 1:
        n -= 1
        if lista[n-1] < minimo:
            minimo = lista[n-1]
    return minimo

print(f'buscar_u_elemento([1,2,3,2,3,4],3)\n{buscar_u_elemento([1,2,3,2,3,4],3)}')
print(f'buscar_n_elemento([1,2,3,2,3,4],3)\n{buscar_n_elemento([1,2,3,2,3,4],3)}')
print(f'maximo([1,2,7,2,3,4])\n{maximo([1,2,7,2,3,4])}')
print(f'minimo([-5,-4,3,0,1,-1])\n{minimo([-5,-4,3,0,1,-1])}')
