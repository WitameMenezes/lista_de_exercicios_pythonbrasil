'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

sexo = input('Digite M para Masculino ou F para Feminino: ').upper()
altura = float(input('Digite sua altura em centímetros: '))

peso_M = (72.2 * altura / 100) - 58
peso_F = (62.1 * altura / 100) - 44.7

if sexo == 'M':
    print('Seu peso ideal é {:.2f}.'.format(peso_M))
else:
    print('Seu peso ideal é {:.2f}.'.format(peso_F))
