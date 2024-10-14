#compras web
dinheiro_conta = int(input())
valor_compras = int(input())

if valor_compras <= dinheiro_conta:
    print("pode comprar tudo")
else:
    print("saldo insuficiente")
