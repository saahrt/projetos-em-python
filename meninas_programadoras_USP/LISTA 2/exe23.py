#compras web2
dinheiro_conta = int(input())
valor_compras = int(input())

if valor_compras <= dinheiro_conta:
    saldo = dinheiro_conta - valor_compras 
    print("se você comprar tudo o saldo será:", saldo)
else:
    print("seu saldo é insuficiente para essa compra")