# ordenar_imgs.py
import os
from datetime import datetime

def ordenar_imgs(directorio):
    for root, dirs, filenames in os.walk(directorio):
        for filename in filenames:
            procesar(filename)

def procesar_nombre(fname):
    name, ext = fname.split('.')
    if ext != 'png':
        return None, None
    title, strdate = name.split('_')
    return title + '.' + ext, datetime.strptime(strdate, '%Y%m%d')

def procesar(fname):
    new_fname, parsed_date = procesar_nombre(fname)
    times = (parsed_date.strftime('%s'), parsed_date.strftime('%s'))
    os.uname(fname, times)
    os.rename(fname, os.path.join('..', 'imgs_procesadas', new_fname))

ordenar_imgs()