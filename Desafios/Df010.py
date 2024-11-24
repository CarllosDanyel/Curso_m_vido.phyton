valor=float(input('Digite quantos reais você tem: '))
dolar=valor/5.38
euro=valor/6.37
libra=valor/7.24
print('Com R${:.2f} você pode comprar US${:.2f}, €{:.2f} e £{:.2f}'.format(valor, dolar, euro, libra))

