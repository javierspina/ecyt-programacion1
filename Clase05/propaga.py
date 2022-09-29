#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:49:18 2022

@author: Javier Spina

"""

def propagar(fosforos):
    nuevo = 0
    encendido = 1
    encender = []
    propagacion = list(fosforos)

    for i, f in enumerate(fosforos):
        # busco el fosforo encendido y chequeo los fosforos anteriores y siguientes
        if f == encendido:
            inicio = i
            fin = i

            # chequear anteriores
            n = i - 1
            while n >= 0:
                if fosforos[n] == nuevo or fosforos[n] == encendido:
                    inicio = n
                else:
                    break
                n -= 1

            # chequear siguientes
            n = i + 1
            while n < len(fosforos):
                if fosforos[n] == nuevo or fosforos[n] == encendido:
                    fin = n
                else:
                    break
                n += 1

            # marcar inicio y fin de slice a cambiar
            encender.append((inicio, fin))

            # omitir iteraciones si ya se chequeó el fin de la lista
            if fin == len(fosforos) - 1:
                break

    # propagar fuego
    for indices in encender:
        i, f = indices
        propagacion[i:f+1] = [1] * (f+1-i)
    return propagacion


print(f'propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])\n{propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])}')
print(f'propagar([ 0, 0, 0, 1, 0, 0])\n{propagar([ 0, 0, 0, 1, 0, 0])}')
