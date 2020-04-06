class Veiculo():
	'''Classe Veiculo. Abstrái caracteristicas de um veiculo. '''
	def __init__(self, cor, tipo_combustivel, potencia):
		self._cor = cor
		self._tipo_combustivel = tipo_combustivel
		self._potencia = potencia
		self._qtd_combustivel = 0
		self._is_ligado = False
		self._velocidade = 0
	
	def abastecer(self, qtd_combustivel):
	    self._qtd_combustivel += qtd_combustivel
	
	def ligar(self):
		if(self._is_ligado):
			print('o Veiculo já está ligado')
		else:
			self._is_ligado = True
			print('o Veiculo foi ligado')
	
	def desligar(self):
		if(self._is_ligado):
			self._is_ligado = False
			print('o Veiculo foi desligado')
		else:
			print('o Veiculo já está desligado')
	def acelerar(self, velocidade=10):
		if self._is_ligado:
			self._velocidade += velocidade
		else:
			print('O carro está desligado')