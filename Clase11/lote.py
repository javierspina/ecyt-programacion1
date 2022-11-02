# lote.py


class Lote:
    def __init__(self, nombre:str, cajones:int, precio:float) -> None:
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def __repr__(self):
        return f'Lote("{self.nombre}", {self.cajones}, {self.precio})'

    def costo(self) -> float:
        return self.cajones * self.precio

    def vender(self, cajones:int) -> None:
        self.cajones -= cajones
