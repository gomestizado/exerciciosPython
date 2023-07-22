metro = float(input('Digite um tamanho em metros: '))

decametro = metro / 10
hectometro = metro / 100
quilometro = metro / 1000

decimetro = metro * 10
centimetro = metro * 100
milimetro = metro * 1000

print('\n===== RESULTADO =====')
print ('\nDecâmetro:     {:.3f}dam\nHectômetro:    {:.3f}hm\nQuilômetro:    {:.3f}km\n\nMETRO:         {:.0f}m\n\nDecímetro:     {:.0f}dm\nCentímetro:    {:.0f}cm\nMilímetro:     {:.0f}mm'.format(decametro, hectometro, quilometro, metro, decimetro, centimetro, milimetro))
