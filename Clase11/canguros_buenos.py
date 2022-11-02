# canguros_buenos.py

# %%


class Canguro:
    def __init__(self, nombre:str, contenido:list = []) -> None:
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy()
        # sin .copy(), todas las instancias de Canguro apuntaban a la misma
        # dirección de memoria de no ser inicializadas

    def __str__(self) -> str:
        cont = [object.__str__(c) for c in self.contenido_marsupio]
        txt = f'Soy {self.nombre} y en mi marsupio tengo:\n' + '\n'.join(cont)
        return txt

    def meter_en_marsupio(self, objeto) -> None:
        self.contenido_marsupio.append(objeto)

# %%


# class Canguro:
#     """Un Canguro es un marsupial."""

#     def __init__(self, nombre, contenido=[]):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         self.contenido_marsupio = contenido.copy()

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [self.nombre + ' tiene en su marsupio:']
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)

madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)
