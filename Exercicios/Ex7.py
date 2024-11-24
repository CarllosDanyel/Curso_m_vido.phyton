from math import sqrt, floor
import emoji

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

# Adicionando um emoji à saída
print(emoji.emojize('Cálculo concluído :thumbs_up:'))
