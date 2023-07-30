frase = str(input('Digite uma frase: ')).lower().strip()

print('A frase contém {} letras A.'.format(frase.count('a')))
print('A primeira está na posição {}'.format(frase.find('a') + 1))
print('E a última está na posição {}'.format(frase.rfind('a') + 1))
