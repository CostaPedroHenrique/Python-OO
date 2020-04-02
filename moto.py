import veiculo
class Moto(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print('Abastecendo moto')
        if self.qtd_combustivel >=30:
            print('O tanque está cheio')
        else:
            self.qtd_combustivel += qtd_combustivel