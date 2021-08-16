'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
  - Salário Bruto até 900 (inclusive) - isento
  - Salário Bruto até 1500 (inclusive) - desconto de 5%
  - Salário Bruto até 2500 (inclusive) - desconto de 10%
  - Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

  Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00
'''

valor_hora_trabalhada = float(input('Digite o valor, em Reais, da sua hora de trabalho: R$ '))
quantidade_hora_trabalhada = float(input('Digite a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora_trabalhada * quantidade_hora_trabalhada

desc_imp_renda1 = 0
desc_imp_renda2 = salario_bruto * 0.05
desc_imp_renda3 = salario_bruto * 0.10
desc_imp_renda4 = salario_bruto * 0.20

desc_sind = salario_bruto * 0.03

desc_inss = salario_bruto * 0.10

dep_fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    print('Salário Bruto: R$ {:.2f}.'.format(salario_bruto))
    print('(-) Imposto de Renda: R$ {:.2f}.'.format(desc_imp_renda1))
    print('(-) INSS: R$ {:.2f}.'.format(desc_inss))
    print('(-) Sindicato: R$ {:.2f}.'.format(desc_sind))
    print('FGTS: R$ {:.2f}.'.format(dep_fgts))
    print('Total de Descontos: R$ {:.2f}.'.format(desc_imp_renda1 + desc_inss + desc_sind))
    print('Salário Líquido: R$ {:.2f}.'.format(salario_bruto - desc_imp_renda1 - desc_inss - desc_sind))
elif salario_bruto <= 1500:
    print('Salário Bruto: R$ {:.2f}.'.format(salario_bruto))
    print('(-) Imposto de Renda: R$ {:.2f}.'.format(desc_imp_renda2))
    print('(-) INSS: R$ {:.2f}.'.format(desc_inss))
    print('(-) Sindicato: R$ {:.2f}.'.format(desc_sind))
    print('FGTS: R$ {:.2f}.'.format(dep_fgts))
    print('Total de Descontos: R$ {:.2f}.'.format(desc_imp_renda2 + desc_inss + desc_sind))
    print('Salário Líquido: R$ {:.2f}.'.format(salario_bruto - desc_imp_renda2 - desc_inss - desc_sind))
elif salario_bruto <= 2500:
    print('Salário Bruto: R$ {:.2f}.'.format(salario_bruto))
    print('(-) Imposto de Renda: R$ {:.2f}.'.format(desc_imp_renda3))
    print('(-) INSS: R$ {:.2f}.'.format(desc_inss))
    print('(-) Sindicato: R$ {:.2f}.'.format(desc_sind))
    print('FGTS: R$ {:.2f}.'.format(dep_fgts))
    print('Total de Descontos: R$ {:.2f}.'.format(desc_imp_renda3 + desc_inss + desc_sind))
    print('Salário Líquido: R$ {:.2f}.'.format(salario_bruto - desc_imp_renda3 - desc_inss - desc_sind))
else:
    print('Salário Bruto: R$ {:.2f}.'.format(salario_bruto))
    print('(-) Imposto de Renda: R$ {:.2f}.'.format(desc_imp_renda4))
    print('(-) INSS: R$ {:.2f}.'.format(desc_inss))
    print('(-) Sindicato: R$ {:.2f}.'.format(desc_sind))
    print('FGTS: R$ {:.2f}.'.format(dep_fgts))
    print('Total de Descontos: R$ {:.2f}.'.format(desc_imp_renda4 + desc_inss + desc_sind))
    print('Salário Líquido: R$ {:.2f}.'.format(salario_bruto - desc_imp_renda4 - desc_inss - desc_sind))

