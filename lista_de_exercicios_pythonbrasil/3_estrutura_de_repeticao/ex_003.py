'''
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''


nome = str(input('Digite o seu nome: '))



idade = int(input('Digite a sua idade: '))
'''
salario = float(input('Digite o seu salário: R$ '))
sexo = str(input('Informe seu sexo: '))
estado_civil = str(input('Informe seu Estado Civíl: '))
'''

while len(nome) <= 3:
    nome = str(input('Digite o seu nome: '))


