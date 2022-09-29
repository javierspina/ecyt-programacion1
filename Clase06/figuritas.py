'''
figuritas.py
Wed Sep 14 21:30:53 2022
Autor: Javier Spina
'''
import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

def album_incompleto(A):
    return A[A == 0].size != 0

def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

def pegar_figu(album, figu):
    if album[figu] == 0:
        album[figu] = 1

def cuantas_figus(figus_total):
    mi_album = crear_album(figus_total)
    # simular llenado
    n_compras = 0
    while album_incompleto(mi_album):
        nueva_figu = comprar_figu(figus_total)
        pegar_figu(mi_album, nueva_figu)
        n_compras += 1
    # devolver cantidad de figuritas que se necesitaron para llenar el album
    return n_compras

def experimento_figus(n_repeticiones, figus_total):
    return np.array([cuantas_figus(figus_total) for i in range(n_repeticiones)])

def comprar_paquete(figus_total, figus_paquete):
    return np.array([comprar_figu(figus_total) for i in range(figus_paquete)])

def cuantos_paquetes(figus_total, figus_paquete):
    # generar album nuevo
    mi_album = crear_album(figus_total)
    # simular llenado
    n_paquetes = 0
    while album_incompleto(mi_album):
        nuevo_paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in nuevo_paquete:
            pegar_figu(mi_album, figu)
        n_paquetes += 1
    # cuantos paquetes se necesitaron para llenar
    return n_paquetes

def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    return np.array([cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)])

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete).tolist()
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

figus_total = 670
experimentos_figus = 1000
promedio_figus = experimento_figus(experimentos_figus, figus_total).mean()
print(f'Para un album de {figus_total} figus, simulando {experimentos_figus} veces, se necesitó comprar en promedio {promedio_figus} figus')

experimentos_paquetes = 1000
figus_paquete = 5
promedio_paquetes = experimento_paquetes(experimentos_paquetes, figus_total, figus_paquete).mean()
print(f'Para un album de {figus_total} figus, con paquetes de {figus_paquete} figus, simulando {experimentos_paquetes} veces, se necesitó comprar en promedio {promedio_paquetes} paquetes')


plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
