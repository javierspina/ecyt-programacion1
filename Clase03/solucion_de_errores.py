'''
solucion_de_errores.py
Ejercicios de errores en el código
'''
#%%
'''
Ejercicio 3.5:
    Al usar return en el if-else statement, el ciclo analizaba sólo el primer caracter. Se corrigió incorporando la variable "a_presente", iniciada en False antes del ciclo y evaluando cada caracter (lineas 14, 17 y 19)
    Se hizo que la función no sea case-sensitive agregando str.lower() en el condicional (linea 16)
'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    a_presente = False
    while i<n:
        if expresion[i].lower() == 'a':
            a_presente = True
        i += 1
    return a_presente

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
'''
Ejercicio 3.6:
    Todos los ":" faltaban (lineas 32, 35, 36). También, en la condición del if se estaba asignando con "=" en vez de evaluar con "=="
    "Falso" no es el nombre correcto para el valor de verdad buscado. Se reemplazo por "False" (linea 37)
    Se agregó también el str.lower() (linea 35)
'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
'''
Ejercicio 3.7:
    La invocación a tiene_uno debe ser con un String como argumento, ya que se necesita obtener una longitud para el bucle (linea 65)
'''

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')

#%%
'''
Ejercicio 3.8:
    La función suma no tiene return, por lo que la asignación de c = suma(a,b) no le da el valor esperado a c (linea 72)
'''

def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
'''
Ejercicio 3.9:
    Al crear la dirección de memoria para registro afuera del ciclo, se crea una sola vez y con cada iteración se cambia los valores únicos que se crearon. El append solo clona la variable única registro.
    Se soluciona moviendo la declaración registro = {} como primera linea del ciclo for (linea 95)
'''

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)