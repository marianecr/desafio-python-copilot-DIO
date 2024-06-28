'''Receber um texto do usuário e repetir esse texto 10 vezes na tela.'''

# Recebendo o texto do usuário
texto = input("Digite um texto: ").strip()  # strip() remove espaços em branco no início e no final da string

# Repetindo o texto 10 vezes
print((texto + ' ') * 10)  

# O espaço em branco é para separar as palavras. Se não colocar, as palavras ficarão juntas.
# O operador * é usado para repetir uma string n vezes. Nesse caso, o texto é repetido 10 vezes.
# O operador + é usado para concatenar strings. Nesse caso, o texto é concatenado com um espaço em branco.
