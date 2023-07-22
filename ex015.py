km = float(input('Digite os Km rodados: '))
d = float(input('Digite os dias alugados: '))

conta = 60*d + 0.15*km

print('O total é R${:.2f}'.format(conta))
