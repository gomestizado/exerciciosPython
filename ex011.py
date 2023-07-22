altura = float(input('Altura: '))
largura = float(input('Largura: '))

area = altura * largura
tinta = area / 2

print('\nSerá necessário {:.1f}L de tinta para pintar um total de {:.1f}m²\n'.format(tinta, area))
