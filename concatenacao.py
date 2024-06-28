'''Receber duas informações do usuário e mostrar na tela utilizando o f string.'''

# Recebendo as informações do usuário
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

# Mostrando as informações
print(f'Seu nome é {nome} e você tem {idade} anos.')

# O f string é uma forma mais simples e legível de formatar strings no Python.
# Ele é utilizado para inserir variáveis dentro de strings.
# Para usar o f string, basta colocar a letra f antes das aspas.
# Dentro das chaves, coloque a variável que deseja inserir na string.
