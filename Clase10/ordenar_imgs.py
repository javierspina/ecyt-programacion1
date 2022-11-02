# ordenar_imgs.py
import os
from datetime import datetime

def ordenar_imgs(directorio:str) -> None:
    '''
    Recorre el directorio y procesa los pngs: renombra y mueve
    '''
    for root, dirs, filenames in os.walk(directorio):
        for filename in filenames:
            procesar(root, filename)
        for d in dirs:
            d = os.path.join(root, d)
            if len(os.listdir(d)) == 0:
                os.rmdir(d)

def procesar_nombre(fname:str) -> tuple:
    '''
    Toma un nombre de archivo y devuelve el nuevo nombre y un datetime
    '''
    name, ext = fname.split('.')
    if ext != 'png':
        return None, None
    title = []
    for part in name.split('_'):
        try:
            strdate = int(part)
        except ValueError as e:
            print(f'[INFO]: {e}')
            title.append(part)
    return '_'.join(title) + '.' + ext, datetime.strptime(str(strdate), '%Y%m%d')

def procesar(root:str, fname:str) -> None:
    '''
    Cambia el nombre del archivo y lo mueve
    '''
    new_fname, parsed_date = procesar_nombre(fname)
    if new_fname == None:
        return
    fname = os.path.join(root, fname)
    new_fname = os.path.join('..', 'Data', 'imgs_procesadas', new_fname)
    times = (int(parsed_date.strftime('%s')), int(parsed_date.strftime('%s')))
    os.utime(fname, times)
    os.rename(fname, new_fname)

# ordenar_imgs('../Data/ordenar')
