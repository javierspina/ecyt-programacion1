# formato_tabla.py

def crear_formateador(formato):
    if formato == 'txt':
        formateador = FormatoTablaTXT()
    elif formato == 'csv':
        formateador = FormatoTablaCSV()
    elif formato == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {formato}')
    return formateador

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rows):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()


class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))


class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print(''.join(['<tr>', *[f'<th>{h}</th>' for h in headers], '</tr>']))

    def fila(self, data_fila):
        print(''.join(['<tr>', *[f'<td>{d}</td>' for d in data_fila], '</tr>']))