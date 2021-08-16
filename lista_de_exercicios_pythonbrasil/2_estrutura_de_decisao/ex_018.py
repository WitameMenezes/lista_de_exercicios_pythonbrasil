'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''

dia = int(input('Digite um dia - 01 a 31: '))
mes = int(input('Digite um mês - 01 a 12: '))
ano = int(input('Digite um ano: '))

print('A data é {}/{}/{}.'.format(dia, mes, ano))
