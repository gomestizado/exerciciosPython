nome = str(input('Digite seu nome completo: ')).strip()

nome = nome.split()

print('\nSeu primeiro nome é {}\nE o seu ultimo nome é {}'.format(nome[0].capitalize(), nome[-1].capitalize()))

#print('\nSeu primeiro nome é {}\nE o seu ultimo nome é {}'.format(nome[0].capitalize(), nome[len(nome)-1].capitalize()))
     