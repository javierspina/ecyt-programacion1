"""
cronica.py

Contador de días faltantes para la próxima primavera

Disclaimer científico: Primavera del hemisferio sur.
Se tiene en cuenta el día festivo 21 de septiembre como primavera,
no el equinoccio de septiembre.
"""
import datetime

def dias_restantes_proxima_primavera() -> str:
    '''
    Indica cuántos días faltan para la próxima primavera
    '''
    hoy = datetime.datetime.today()
    prox_primavera = datetime.datetime(hoy.year + 1, 9, 21)
    dias_restantes = (prox_primavera - hoy).days
    return f'¡Faltan {dias_restantes} días para la primavera!'
