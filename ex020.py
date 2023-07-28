from random import shuffle

a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto nome: ')

alunos = [a1 , a2 , a3 , a4]

shuffle(alunos)

print('\nA ordem de apresentação será:')
print('1 - {}\n2 - {}\n3 - {}\n4 - {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
