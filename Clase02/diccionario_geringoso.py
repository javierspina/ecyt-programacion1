'''
diccionario_geringoso.py
Autor: Javier Spina
Ejercicio 2.13, Clase 2
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
2022-08-07
'''

def geringar_silaba(vocal):
    return vocal + 'p' + vocal

def geringar_palabra(palabra):
    vocales = 'aeiouáéíóú'
    capadepenapa = ''
    for letra in palabra:
        if letra in vocales:
            capadepenapa += geringar_silaba(letra)
        else:
            capadepenapa += letra
    return capadepenapa

def diccionario_geringoso(lista):
    d = {}
    for palabra in lista:
        d[palabra] = geringar_palabra(palabra)
    return d

print(diccionario_geringoso(['banana', 'manzana', 'mandarina']))

'''
stdout:
    
{
 'banana': 'bapanapanapa', 
 'manzana': 'mapanzapanapa', 
 'mandarina': 'mapandaparipinapa'
 }
'''