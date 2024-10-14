# Seu programa deve ler um valor inteiro, correspondente a um ano (e.g. 2023),
# calcular qual o século correspondente (e.g. 21), e imprimir o valor calculado.

ano = int(input())
if ano % 100 == 0:
    seculo = ano // 100
    print(seculo)
else:
    seculo = (ano // 100) + 1
    print(seculo)
