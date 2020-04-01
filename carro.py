class Carro():
	def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
		self.cor = cor
		self.qtd_portas = qtd_portas
		self.tipo_combustivel = tipo_combustivel
		self.potencia = potencia
		self.qtd_combustivel = qtd_combustivel
		self.is_ligado = is_ligado
		self.velocidade = velocidade

	
	def abastecer(self, qtd_combustivel):
	    self.qtd_combustivel += qtd_combustivel
	
	def ligar(self):
		if(self.is_ligado):
			print('o carro já está ligado')
		else:
			self.is_ligado = True
			print('o carro foi ligado')
	
	def desligar(self):
		if(self.is_ligado):
			self.is_ligado = False
			print('o carro foi desligado')
		else:
			print('o carro já está desligado')
	def acelerar(self, velocidade=10):
		if self.is_ligado:
			self.velocidade += velocidade
		else:
			print('O carro está desligado')