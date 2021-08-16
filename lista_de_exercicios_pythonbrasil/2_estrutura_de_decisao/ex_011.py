'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5%.

Após o aumento ser realizado, informe na tela:
    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento.
'''

salario = float(input('Digite o seu salário: R$ '))

aumento1 = salario * 0.2
aumento2 = salario * 0.15
aumento3 = salario * 0.1
aumento4 = salario * 0.05

sal1 = salario + aumento1
sal2 = salario + aumento2
sal3 = salario + aumento3
sal4 = salario + aumento4

if salario <= 280:
    print('- Salário antes do reajuste: R$ {:.2f}.'.format(salario))
    print('- Percentual de aumento aplicado: 20%')
    print('- Valor do aumento: R$ {:.2f}'.format(aumento1))
    print('- Novo salário: R$ {:.2f}'.format(sal1))
elif salario > 280 and salario <= 700:
    print('- Salário antes do reajuste: R$ {:.2f}.'.format(salario))
    print('- Percentual de aumento aplicado: 15%')
    print('- Valor do aumento: R$ {:.2f}'.format(aumento2))
    print('- Novo salário: R$ {:.2f}'.format(sal2))
elif salario > 700 and salario <= 1500:
    print('- Salário antes do reajuste: R$ {:.2f}.'.format(salario))
    print('- Percentual de aumento aplicado: 10%')
    print('- Valor do aumento: R$ {:.2f}'.format(aumento3))
    print('- Novo salário: R$ {:.2f}'.format(sal3))
elif salario > 1500:
    print('- Salário antes do reajuste: R$ {:.2f}.'.format(salario))
    print('- Percentual de aumento aplicado: 5%')
    print('- Valor do aumento: R$ {:.2f}'.format(aumento4))
    print('- Novo salário: R$ {:.2f}'.format(sal4))

