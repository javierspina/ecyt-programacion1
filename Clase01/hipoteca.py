'''
hipoteca.py
Autor: Javier Spina
Ejercicio 1.11, Clase 1
Programación 1 - Licenciatura en Ciencia de Datos - ECyT UNSAM
2022-08-07
'''

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 1

# variables versatiles
pago_extra = float(input('¿Cuánto es el adelanto?\n'))
pago_extra_mes_comienzo = int(input('¿Cuál es el mes en que se comienza el pago extra?\n'))
pago_extra_mes_fin = int(input('¿En que mes se finaliza el adelanto?\n'))

while saldo > 0:
    pago_actual = pago_mensual
    if meses >= pago_extra_mes_comienzo and meses <= pago_extra_mes_fin:
        pago_actual += pago_extra
    saldo = saldo * (1+tasa/12) - pago_actual
    if saldo < pago_actual:
        pago_actual = saldo
        saldo = 0
    total_pagado = total_pagado + pago_actual
    print(f'{meses} {round(pago_actual, ndigits=2)} {round(saldo, ndigits=2)}')
    meses += 1

print(f'Total pagado {round(total_pagado, 2)}\nMeses requeridos {meses-1}')

'''
¿Cuánto es el adelanto?
1000
¿Cuál es el mes en que se comienza el pago extra?
61
¿En que mes se finaliza el adelanto?
108
1 2684.11 499399.22
2 2684.11 498795.94
...
61 3684.11 457372.52
...
108 3684.11 365253.54
109 2684.11 364091.32
...
307 2684.11 6137.36
308 2684.11 3478.83
309 809.21 0
Total pagado 875515.09
Meses requeridos 309
'''