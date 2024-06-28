'''Receber quatro notas de um aluno, calcular a média e mostrar na tela.'''

# Recebendo as notas do aluno
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

# Calculando a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Mostrando a média
print(f'A média do aluno é: {media:.1f}')
