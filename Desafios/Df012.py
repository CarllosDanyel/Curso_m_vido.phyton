Preco=float(input('Digite o preço do produto: R$'))
Desconto=Preco*0.05
Desconto=Preco-Desconto
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(Preco, Desconto))
