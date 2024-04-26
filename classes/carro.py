from classes.veiculo_pai import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas=0):
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'{self._marca} | {self._modelo} | {self._portas} - Status: {status}'