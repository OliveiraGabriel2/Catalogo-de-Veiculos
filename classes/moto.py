from classes.veiculo_pai import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'{self._marca} | {self._modelo} | {self._tipo} - Status: {status}'