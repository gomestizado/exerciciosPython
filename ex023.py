#1ª FORMA
"""numero = list(str(input('Digite um número: ')))

numero.insert(0, '0')
numero.insert(0, '0')
numero.insert(0, '0')
numero.insert(0, '0')

print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(numero[-1], numero[-2], numero[-3], numero[-4]))"""


#2ª FORMA
zeros = ['0', '0', '0', '0']
numero = list(str(input('Digite um número: ')))

zeros.extend(numero)

print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(zeros[-1], zeros[-2], zeros[-3], zeros[-4]))


#3ª FORMA - resposta do video
"""numero = int(input('Digite um número: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n'.format(u, d, c, m))"""
