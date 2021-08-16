'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dia_da_semana = int(input('Digite um número de 1 a 7 e saiba qual o dia da semana correspondente ao número digitado: '))

dia1 = 'Domingo'
dia2 = 'Segunda'
dia3 = 'Terça'
dia4 = 'Quarta'
dia5 = 'Quinta'
dia6 = 'Sexta'
dia7 = 'Sábado'

if dia_da_semana == 1:
    print('O dia da semana correspondente é {}.'.format(dia1))
elif dia_da_semana == 2:
    print('O dia da semana correspondente é {}.'.format(dia2))
elif dia_da_semana == 3:
    print('O dia da semana correspondente é {}.'.format(dia3))
elif dia_da_semana == 4:
    print('O dia da semana correspondente é {}.'.format(dia4))
elif dia_da_semana == 5:
    print('O dia da semana correspondente é {}.'.format(dia5))
elif dia_da_semana == 6:
    print('O dia da semana correspondente é {}.'.format(dia6))
elif dia_da_semana == 7:
    print('O dia da semana correspondente é {}.'.format(dia7))
else:
    print('Valor inválido.')
