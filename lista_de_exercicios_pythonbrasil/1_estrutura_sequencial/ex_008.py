'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

salario_hora = float(input('Digite o valor qua você ganha por hora trabalhada: R$ '))
horas_trabalhadas = float(input('Digite a quantidade horas trabalhadas neste mês: '))

salario_mes = salario_hora * horas_trabalhadas

print(f'De acordo com os dados informados, seu salário é de R$ {salario_mes:.2f}.')
print('De acordo com os dados informados, seu salário é de R$ {:.2f}.'.format(salario_mes))
