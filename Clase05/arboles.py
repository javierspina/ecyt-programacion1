'''
arboles.py
Autor: Javier Spina
Agosto 2022
ECyT UNSAM - Programación 1
'''
import csv
from collections import Counter
from statistics import mean
from pprint import pprint


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
    return max([(mean(obtener_inclinaciones(lista_arboles, especie)), especie)
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


arboleda = leer_arboles('../Data/arbolado.csv')

alturas_jacaranda = [arbol['altura_tot'] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
pprint(alturas_jacaranda)

medidas_jacaranda = [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
pprint(medidas_jacaranda)

lista_especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
pprint(medidas_de_especies(lista_especies, arboleda))
