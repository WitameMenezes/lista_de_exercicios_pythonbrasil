'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''

bim_1 = float(input('Digite a primeira nota bimestral: '))
bim_2 = float(input('Digite a segunda nota bimestral: '))
bim_3 = float(input('Digite a terceira nota bimestral: '))
bim_4 = float(input('Digite a quarta nota bimestral: '))

media = (bim_1 + bim_2 + bim_3 + bim_4) / 4

print(f'A média das notas {bim_1}, {bim_2}, {bim_3} e {bim_4} é {media}.')
print('A média das notas {}, {}, {} e {} é {}.'.format(bim_1, bim_2, bim_3, bim_4, media))
