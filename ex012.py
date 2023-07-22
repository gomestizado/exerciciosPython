preco = float(input('Digite o preço do produto: R$'))

desconto = preco - (preco*5 / 100) 

print('Com desconto de 5% fica R${:.2f}'.format(desconto))
