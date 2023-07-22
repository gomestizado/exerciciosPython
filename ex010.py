real = float(input('\nQuantos reais você tem na carteira? R$'))

dolar = real / 3.27

print('\nCom R${:.2f} é possível comprar US${:.2f}\n'.format(real, dolar))