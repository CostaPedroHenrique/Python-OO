import carro
import moto

uno_preto = carro.Carro('preto', 'flex',1.4, 2)

uno_preto.abastecer(50)
print(f"A quantidade de combustivel é: {uno_preto.qtd_combustivel}")
uno_preto.ligar()
uno_preto.acelerar(20);
print('Velocidade: {}'.format(uno_preto.velocidade))

biz = moto.Moto('vermelha', 'gasolina', 1.0, 2);
biz.ligar()