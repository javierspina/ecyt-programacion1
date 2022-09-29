#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:38:56 2022

@author: Javier Spina
"""

def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida = [e] + invertida
    return invertida

ciudades = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(f'invertir_lista({ciudades})\n{invertir_lista(ciudades)}')
