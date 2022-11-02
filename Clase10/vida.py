# vida.py
import datetime

def vida_en_segundos(fecha_nac:str) -> float:
    '''
    Tiempo vivido en segundos.
    Toma una fecha de nacimiento con formato string "dd/mm/yyyy",
    y devuelve la diferencia de tiempo en segundos con el día de hoy
    '''
    hoy = datetime.datetime.today()
    nac = datetime.datetime.strptime(fecha_nac, '%d/%m/%Y')
    return (hoy - nac).total_seconds()
