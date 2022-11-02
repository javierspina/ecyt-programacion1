# torre_control.py

class Pista:
    """
    Representa una pista de un aeropuerto.
    """

    def __init__(self) -> None:
        """
        Crea una nueva pista.
        """
        self.pista = list()
        self.tipo = ''

    def __str__(self):
        return f'Vuelos esperando para {self.tipo}: {", ".join(self.pista)}'

    def encolar(self, tailnum:str) -> None:
        """
        Encola a tailnum en la pista.
        """
        self.pista.append(tailnum)

    def desencolar(self) -> str:
        """
        Desencola a tailnum de la pista.
        """
        if self.esta_vacia():
            raise ValueError(f'La pista para {self.tipo} está vacía.')
        return self.pista.pop(0)

    def esta_vacia(self) -> bool:
        """
        Valida si la pista está vacía.
        """
        return len(self.pista) == 0


class PistaAterrizaje(Pista):
    """
    Representa una pista de aterrizajes de un aeropuerto.
    """

    def __init__(self) -> None:
        """
        Crea una nueva pista.
        """
        super().__init__()
        self.tipo = 'aterrizar'

    def aterrizar(self) -> str:
        """
        Aterriza al primer avión de la cola.
        """
        return f'El vuelo {super().desencolar()} aterrizó con éxito.'


class PistaDespegue(Pista):
    """
    Representa una pista de despegues de un aeropuerto.
    """

    def __init__(self) -> None:
        """
        Crea una nueva pista
        """
        super().__init__()
        self.tipo = 'despegar'

    def despegar(self) -> str:
        """
        Despega el primer avión de la cola.
        """
        return f'El vuelo {super().desencolar()} despegó con éxito.'


class TorreDeControl:
    """
    Representa una torre de control de un aeropuerto.
    """

    def __init__(self) -> None:
        """
        Crea una nueva torre de control.
        """
        self.pista_despegue = PistaDespegue()
        self.pista_aterrizaje = PistaAterrizaje()

    def nuevo_arribo(self, tailnum:str) -> None:
        """
        Encola a tailnum para la pista de aterrizaje.
        """
        self.pista_aterrizaje.encolar(tailnum)

    def nueva_partida(self, tailnum:str) -> None:
        """
        Encola a tailnum para la pista de despegue.
        """
        self.pista_despegue.encolar(tailnum)

    def ver_estado(self) -> None:
        """
        Reporta el estado de las pistas.
        """
        print(self.pista_aterrizaje, self.pista_despegue, sep='\n')

    def asignar_pista(self) -> None:
        """
        Autoriza aterrizajes y despegues.
        Avanzan con priorirdad los aterrizajes.
        De no haber vuelos por aterrizar, despegan los aviones.
        """
        try:
            print(self.pista_aterrizaje.aterrizar())
        except ValueError as e:
            print(f'[INFO] {e}')
            try:
                print(self.pista_despegue.despegar())
            except ValueError as e:
                print(f'[INFO] {e}')
