'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

num = float(input('Digite um número inteiro: '))

if num >= 0:
    print('O número {} é positivo.'.format(num))
else:
    print('O número {} é negativo.'.format(num))
