'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.

A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = (nota1 + nota2) / 2

conceito_a = 'A'
conceito_b = 'B'
conceito_c = 'C'
conceito_d = 'D'
conceito_e = 'E'

resultado_aprovado = 'APROVADO'
resultado_reprovado = 'REPROVADO'

if media <= 4:
    print('A primeira nota é {:.1f}.'.format(nota1))
    print('A segunda nota é {:.1f}.'.format(nota2))
    print('A média das notas é {:.1f}.'.format(media))
    print('O conceito é {}.'.format(conceito_e))
    print('O resultado é {}.'.format(resultado_reprovado))
elif media > 4 and media < 6:
    print('A primeira nota é {:.1f}.'.format(nota1))
    print('A segunda nota é {:.1f}.'.format(nota2))
    print('A média das notas é {:.1f}.'.format(media))
    print('O conceito é {}.'.format(conceito_d))
    print('O resultado é {}.'.format(resultado_reprovado))
elif media >= 6 and media < 7.5:
    print('A primeira nota é {:.1f}.'.format(nota1))
    print('A segunda nota é {:.1f}.'.format(nota2))
    print('A média das notas é {:.1f}.'.format(media))
    print('O conceito é {}.'.format(conceito_c))
    print('O resultado é {}.'.format(resultado_aprovado))
elif media >= 7.5 and media < 9:
    print('A primeira nota é {:.1f}.'.format(nota1))
    print('A segunda nota é {:.1f}.'.format(nota2))
    print('A média das notas é {:.1f}.'.format(media))
    print('O conceito é {}.'.format(conceito_b))
    print('O resultado é {}.'.format(resultado_aprovado))
else:
    print('A primeira nota é {:.1f}.'.format(nota1))
    print('A segunda nota é {:.1f}.'.format(nota2))
    print('A média das notas é {:.1f}.'.format(media))
    print('O conceito é {}.'.format(conceito_a))
    print('O resultado é {}.'.format(resultado_aprovado))

