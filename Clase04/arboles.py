'''
arboles.py
Autor: Javier Spina
Agosto 2022
ECyT UNSAM - Programación 1
'''
import csv
from collections import Counter
from pprint import pprint


def leer_parque(nombre_archivo, parque):
    # Ejercicio 4.13
    trees = []
    with open(nombre_archivo, 'rt') as src:
        rows = csv.reader(src)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            tree = dict(zip(headers, row))
            if tree['espacio_ve'] == parque:
                trees.append(tree)
    return trees


def especies(lista_arboles):
    # Ejercicio 4.14
    name_list = []
    for i, row in enumerate(lista_arboles, start=1):
        name_list.append(row['nombre_com'])
    return set(name_list)


def contar_ejemplares(lista_arboles):
    # Ejercicio 4.15
    specimen_count = Counter()
    for i, row in enumerate(lista_arboles, start=1):
        specimen_count[row['nombre_com']] += 1
    return specimen_count


def obtener_caracteristica(lista_arboles, especie, caracteristica):
    carac = []
    for i, row in enumerate(lista_arboles, start=1):
        if row['nombre_com'] == especie:
            carac.append(float(row[caracteristica]))
    return carac


def obtener_alturas(lista_arboles, especie):
    # Ejercicio 4.16
    return obtener_caracteristica(lista_arboles, especie, 'altura_tot')
    

def obtener_inclinaciones(lista_arboles, especie):
    # Ejercicio 4.17
    return obtener_caracteristica(lista_arboles, especie, 'inclinacio')


def especimen_mas_caracteristico(lista_arboles, caracteristicas):
    specimen_list = especies(lista_arboles)
    max_from_list = 0.0
    max_specimen = ''
    for specimen in specimen_list:
        record = caracteristicas(lista_arboles, specimen)
        if max(record) > max_from_list:
            max_from_list = max(record)
            max_specimen = specimen
    return max_from_list, max_specimen


def especimen_mas_inclinado(lista_arboles):
    # Ejercicio 4.18
    return especimen_mas_caracteristico(lista_arboles, obtener_inclinaciones)


def especimen_mas_alto(lista_arboles):
    return especimen_mas_caracteristico(lista_arboles, obtener_alturas)


def especie_promedio_mas_inclinada(lista_arboles):
    # Ejercicio 4.19
    specimen_list = especies(lista_arboles)
    rank1_avg_lean = 0.0
    rank1_avg_name = ''
    for specimen in specimen_list:
        leanings = obtener_inclinaciones(lista_arboles, specimen)
        avg = sum(leanings) / len(leanings)
        if avg > rank1_avg_lean :#and specimen != 'No Determinable':
            rank1_avg_lean = avg
            rank1_avg_name = specimen
    return rank1_avg_name, rank1_avg_lean


def parques(nombre_archivo):
    parks = []
    with open(nombre_archivo, 'rt') as src:
        rows = csv.reader(src)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            parks.append(dict(zip(headers, row))['espacio_ve'])
    return set(parks)

#%%
# Reportes:

nombre_archivo = '../Data/arbolado.csv'

gral_paz = leer_parque('../Data/arbolado.csv', 'GENERAL PAZ')

especies_gral_paz = especies(gral_paz)

parques_ejemplo = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

for parque in parques_ejemplo:
    dataset = leer_parque('../Data/arbolado.csv', parque)
    print(f'Especies más comunes en el parque {parque.capitalize()}:')
    pprint(contar_ejemplares(dataset).most_common(5))

print('\nInclinaciones de la especie Fénix en Parque Gral Paz')
pprint(obtener_inclinaciones(gral_paz, "Fenix"))

print('\nÁrboles más altos en cada parque y el promedio:')
print('%15s %12s %12s' % (' ', 'max', 'prom'))
for parque in parques_ejemplo:
    dataset = leer_parque('../Data/arbolado.csv', parque)
    heights = obtener_alturas(dataset, 'Jacarandá')
    print(f'{parque.capitalize():15s} {max(heights):10.2f} m {(sum(heights) / len(heights)):10.2f} m')
    
print('\nEspecies más inclinadas:')
for parque in parques_ejemplo:
    dataset = leer_parque('../Data/arbolado.csv', parque)
    most_lean = especimen_mas_inclinado(dataset)
    print('Parque: %s,Inclinación: %.2f, Especie: %s' % (parque, most_lean[0], most_lean[1]))

print('\nEspecies promedio más inclinadas:')
for parque in parques_ejemplo:
    dataset = leer_parque('../Data/arbolado.csv', parque)
    data = especie_promedio_mas_inclinada(dataset)
    print('Parque: %s, Especie: %s, Promedio inclinación: %.2f' % (parque, data[0], data[1]))
