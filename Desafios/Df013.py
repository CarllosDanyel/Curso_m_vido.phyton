Salario=float(input('Digite o salário do funcionário: R$'))
Aumento=Salario*5/100
Aumento=Salario+Aumento
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(Salario, Aumento))
