'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''

preco1 = float(input('Digite o valor do produto 1: R$ '))
preco2 = float(input('Digite o valor do produto 2: R$ '))
preco3 = float(input('Digite o valor do produto 3: R$ '))

if preco1 < preco2 and preco1 < preco3:
    print('O pruduto 1 é o de menor preço, pois custa R$ {}.'.format(preco1))
elif preco2 < preco1 and preco2 < preco3:
    print('O produto 2 é o de menor preço, pois custa R$ {}.'.format(preco2))
else:
    print('O produto 3 é o de menor preço, pois custa R$ {}.'.format(preco3))
