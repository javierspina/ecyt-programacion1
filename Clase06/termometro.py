'''
termometro.py
Autor: Javier Spina
Septiembre 2022
'''
import random
import numpy as np

temp_real = 37.5

def medir_temp(n):
    data = np.array([temp_real + random.normalvariate(0, 0.2) for i in range(n)])
    np.save('../Data/temperaturas.npy', data)
    return data

def resumen_temp(n):
    temps = medir_temp(n)
    resumen = temps.max(), temps.min(), temps.mean(), np.median(temps)
    return resumen

def reportar_temp(n):
    term = resumen_temp(n)
    print(f'Para un paciente con temperatura real de {temp_real}, el termometro arrojó:\nMáxima: {term[0]:.6f} °C\nMínima: {term[1]:.6f} °C\nMedia: {term[2]:.6f} °C\nMediana: {term[3]:.6f} °C')


n = 999
reportar_temp(n)
