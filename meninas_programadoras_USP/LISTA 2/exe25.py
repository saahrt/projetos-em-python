#Seu programa recebe três valores inteiros, um por linha, e deve imprimir True se o último valor estiver 
# contido na faixa estabelecida entre os dois primeiros (inclusive), e False caso contrário.

#entradas
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num3 >= num1 and num3 <= num2:
    print(True)
else:
    print(False)