# listar_imgs.py
import os

def archivos_png(directorio:str) -> list[str]:
    '''
    Busca recursivamente y genera una lista de archivos png.

    Parámetros
    ----------
    directorio : str
        Directorio raíz en el cual se quiere buscar.

    Devuelve
    --------
    list[str]
        Todos los archivos png contenidos en directorio y los subdirectorios.

    '''
    return [filename for root, dirs, filenames in os.walk(directorio)
            for filename in filenames
            if filename.split('.')[-1] == 'png']

if __name__ == '__main__':
    import sys
    print(archivos_png(sys.argv[1]))
