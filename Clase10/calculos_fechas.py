'''
calculos_fechas.py

Wed Oct 26 15:25:05 2022
Autor: Javier Spina

Cálculos varios con fechas
'''
from datetime import datetime
from datetime import timedelta

def fecha_reincorporacion(inicio_licencia:str, dias_licencia:int) -> str:
    '''
    Calcula la fecha de reincoporación.

    Parámetros
    ----------
    inicio_licencia : str
        Fecha de inicio de la licencia.
        Se espera formato "día/mes/año".
        Usar 4 dígitos para el año
    dias_licencia : int
        Días corridos de licencia.
        No tiene en cuenta fines de semana y feríados.

    Returns
    -------
    str
        Fecha en formato "dd/mm/aaaa" que expresa el día final de la licencia.
    '''
    comienzo = datetime.strptime(inicio_licencia, '%d/%m/%Y')
    licencia = timedelta(dias_licencia)
    reincoporacion = comienzo + licencia
    return f'{reincoporacion.strftime("%d/%m/%Y")}'

def dias_habiles(inicio:str, fin:str, feriados:list[str], sin_fin_de_semana:bool = True) -> list[str]:
    '''
    Genera una lista de días hábiles entre una fecha de inicio y otra de fin.

    Parameters
    ----------
    inicio : str
        Fecha de inicio en formato dd/mm/aaaa
    fin : str
        Fecha de final en formato dd/mm/aaaa
    feriados : list[str]
        Lista de feríados en formato dd/mm/aaaa
    sin_fin_de_semana : bool, optional
        Si es True, quita los Sábados y Domingos de la lista.

    Returns
    -------
    list[str]
        Lista de fechas en formato dd/mm/aaaa

    '''
    formato_fecha = r'%d/%m/%Y'
    dia_inicio = datetime.strptime(inicio, formato_fecha)
    dia_fin = datetime.strptime(fin, formato_fecha)
    feriados = [datetime.strptime(f, formato_fecha).strftime(formato_fecha) for f in feriados]

    habiles = [datetime.strftime(dia_inicio + timedelta(i), formato_fecha) for i in range((dia_fin - dia_inicio).days + 1)]
    for feriado in feriados:
        if feriado in habiles:
            habiles.remove(feriado)
    if sin_fin_de_semana:
        for h in habiles.copy():    # tuve que hacer copy sino ignoraba los domingos de la limpieza
            wday = datetime.strptime(h, formato_fecha).weekday()
            if wday in [5, 6]:
                habiles.remove(h)
    return habiles

feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

print(dias_habiles('10/10/2020', '1/1/2021', feriados))

print(dias_habiles('1/10/2020', '11/10/2020', feriados))
