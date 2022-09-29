'''
arboles.py
Autor: Javier Spina
'''
import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def leer_parque(nombre_archivo, parque):
    lista_parque = None
    with open(nombre_archivo, 'rt') as archivo:
        tipos = [float, float, int, float, float, int, int, str, str, str, str, str, str, str, str, float, float]
        filas = csv.reader(archivo)
        encabezados = next(filas)
        lista_parque = [{col: func(valor)
                         for col, func, valor in zip(encabezados, tipos, fila)}
                        for fila in filas if parque in fila]
    return lista_parque


def especies(lista_arboles):
    return set([fila['nombre_com']
                for fila in lista_arboles])


def contar_ejemplares(lista_arboles):
    contador_ejemplares = Counter()
    for fila in lista_arboles:
        contador_ejemplares[fila['nombre_com']] += 1
    return contador_ejemplares


def obtener_caracteristica(lista_arboles, especie, caracteristica):
    return [fila[caracteristica]
            for fila in lista_arboles if fila['nombre_com'] == especie]


def obtener_alturas(lista_arboles, especie):
    return obtener_caracteristica(lista_arboles, especie, 'altura_tot')


def obtener_inclinaciones(lista_arboles, especie):
    return obtener_caracteristica(lista_arboles, especie, 'inclinacio')


def especimen_mas_caracteristico(lista_arboles, caracteristicas):
    return max([(max(caracteristicas(lista_arboles, especie)), especie)
                for especie in especies(lista_arboles)])


def especimen_mas_inclinado(lista_arboles):
    return especimen_mas_caracteristico(lista_arboles, obtener_inclinaciones)


def especimen_mas_alto(lista_arboles):
    return especimen_mas_caracteristico(lista_arboles, obtener_alturas)


def especie_promedio_mas_inclinada(lista_arboles):
    return max([(np.mean(obtener_inclinaciones(lista_arboles, especie)), especie)
                for especie in especies(lista_arboles)])

def leer_arboles(nombre_archivo):
    arboleda = None
    with open(nombre_archivo, 'rt') as archivo:
        tipos = [float, float, int, float, float, int, int, str, str, str, str, str, str, str, str, float, float]
        filas = csv.reader(archivo)
        encabezados = next(filas)
        arboleda = [{col: func(valor)
                     for col, func, valor in zip(encabezados, tipos, fila)}
                    for fila in filas]
    return arboleda

def medidas_de_especies(especies, arboleda):
    return {especie: [(arbol['altura_tot'], arbol['diametro'])
                      for arbol in arboleda if arbol['nombre_com'] == especie]
            for especie in especies}

def scatter_medidas(medidas, especie):
    plt.scatter(medidas[:, 1], medidas[:, 0], alpha=0.8)
    plt.xlabel(f'Diámetros de {especie} [cm]')
    plt.ylabel(f'Alturas de {especie} [m]')
    plt.title(f'Relación Diámetro - Altura para {especie}')
    plt.show()

arboleda = leer_arboles('../Data/arbolado.csv')

def graficar_histograma_jacarandas():
    alturas_jacaranda = np.array([arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'])
    plt.hist(alturas_jacaranda, bins=50, color='purple')
    plt.xlabel('Alturas de Jacarandás [m]')
    plt.ylabel('Cantidad de Jacarandás')
    plt.title('Histograma de las alturas para Jacarandás de CABA')
    plt.show()

def graficar_scatter_jacarandas():
    medidas_jacaranda = np.array([(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'])
    scatter_medidas(medidas_jacaranda, 'Jacarandá')

def graficar_scatters_ejes_comparados(xmax, ymax):
    if type(xmax) != int and type(ymax) != int:
        return
    lista_especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    dif_medidas = medidas_de_especies(lista_especies, arboleda)
    for k, v in dif_medidas.items():
        plt.xlim(0,xmax)
        plt.ylim(0,ymax)
        scatter_medidas(np.array(v), k)

graficar_histograma_jacarandas()
graficar_scatter_jacarandas()
graficar_scatters_ejes_comparados(200, 60)
