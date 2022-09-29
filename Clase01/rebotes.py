'''
rebotes.py
Autor: Javier Spina
Ejercicio 1.5, Clase 1
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
2022-08-07
'''

altura_inicial = 100    # altura desde la que cae la pelota
energia_rebote = 3/5    # proporcion de energia que la pelota recupera para siguiente rebote

def rebotar(n):
    altura_rebote = altura_inicial
    rebote = 1
    redondeo = 4
    while n > 0:
        altura_rebote = energia_rebote * altura_rebote
        print(rebote, round(altura_rebote, ndigits=redondeo))
        n = n - 1
        rebote = rebote + 1

rebotar(10)

'''
stdout:

1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
'''