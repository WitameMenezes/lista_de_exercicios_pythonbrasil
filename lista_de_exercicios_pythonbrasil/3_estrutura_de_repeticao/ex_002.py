'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

usuario = input('Digite o nome de usuário: ').strip()
senha = input('Digite a senha: ').strip()

while usuario == senha:
    print('Usuario e Senha são iguais. Insira novas informações.')
    usuario = input('Digite o nome de usuário: ').strip()
    senha = input('Digite a senha: ').strip()
else:
    print('Usuário e senha inseridos corretamente.')
