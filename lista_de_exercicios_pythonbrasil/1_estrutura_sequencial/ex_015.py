'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
    a) salário bruto.
    b) quanto pagou ao INSS.
    c) quanto pagou ao sindicato.
    d) o salário líquido.

    e) Calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
'''

salario_hora = float(input('Digite o quanto você ganha por hora trabalhada: R$ '))
hora_trabalhada = float(input('Digite a quantidade de horas trabalhadas neste mês: '))

salario_bruto = salario_hora * hora_trabalhada
imp_renda = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - imp_renda - inss - sindicato

print('+ Salário Bruto: R$ {:.2f};'.format(salario_bruto))
print('- IR: R$ {:.2f};'.format(imp_renda))
print('- INSS: R$ {:.2f};'.format(inss))
print('- Sindicato: R$ {:.2f};'.format(sindicato))
print('= Salário Líquido: R$ {:.2f}.'.format(salario_liquido))
