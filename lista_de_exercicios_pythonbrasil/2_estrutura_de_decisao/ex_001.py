'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('{} é maior do que {}.'.format(num1, num2))
else:
    print('{} é maior do que {}.'.format(num2, num1))
