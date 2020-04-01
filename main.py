import carro

uno_vermelho = carro.Carro('vermelho', 4, 'flex',1.0,0,False,0)

#print(uno_vermelho.cor)

uno_preto = carro.Carro('preto', 2, 'flex',1.4,0,False, 0)

uno_preto.abastecer(50)
print(f"A quantidade de combustivel é: {uno_preto.qtd_combustivel}")
uno_preto.ligar()
uno_preto.acelerar(20);
print('Velocidade: {}'.format(uno_preto.velocidade))
