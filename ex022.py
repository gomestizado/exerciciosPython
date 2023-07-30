nome = str(input('Digite seu nome completo:')).strip()

print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))

print('Total letras: {}'.format(len(nome.replace(' ', ''))))
#print('Total letras: {}'.format(len(nome) - nome.count(' ')))

dividido = nome.split()
print('Letras no primeiro nome: {}'.format(len(dividido[0])))
#print('Letras no primeiro nome: {}'.format(nome.find(' ')))
