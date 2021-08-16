'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        a) comprar apenas latas de 18 litros;
        b) comprar apenas galões de 3,6 litros;
        c) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
        arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

area_pintada = float(input('Digite a área a ser pintada (área em metros quadrados): '))
qtde_litros = area_pintada / 6
qtde_latas = math.ceil(qtde_litros / 18)
qtde_galoes = math.ceil(qtde_litros / 3.6)
preco_lata = qtde_latas * 80
preco_galao = qtde_galoes * 25

print('### SITUAÇÃO 1: COMPRAR APENAS LATAS ### \n Quantidade de Tinta: {:.1f} litros \n Quantidade de Latas: {} \n Preço a pagar: R$ {:.2f} reais'.format(qtde_litros, qtde_latas, preco_lata))
print('### SITUAÇÃO 2: COMPRAR APENAS GALÕES ### \n Quantidade de Tinta: {:.1f} litros \n Quantidade de Galões: {} \n Preço a pagar: R$ {:.2f} reais'.format(qtde_litros, qtde_galoes, preco_galao))
