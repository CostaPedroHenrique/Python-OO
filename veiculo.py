class Veiculo():
	'''Classe Veiculo. Abstrái caracteristicas de um veiculo. '''
	def __init__(self, cor, tipo_combustivel, potencia):
		self.cor = cor
		self.tipo_combustivel = tipo_combustivel
		self.potencia = potencia
		self.qtd_combustivel = 0
		self.is_ligado = False
		self.velocidade = 0
	
	def abastecer(self, qtd_combustivel):
	    self.qtd_combustivel += qtd_combustivel
	
	def ligar(self):
		if(self.is_ligado):
			print('o Veiculo já está ligado')
		else:
			self.is_ligado = True
			print('o Veiculo foi ligado')
	
	def desligar(self):
		if(self.is_ligado):
			self.is_ligado = False
			print('o Veiculo foi desligado')
		else:
			print('o Veiculo já está desligado')
	def acelerar(self, velocidade=10):
		if self.is_ligado:
			self.velocidade += velocidade
		else:
			print('O carro está desligado')