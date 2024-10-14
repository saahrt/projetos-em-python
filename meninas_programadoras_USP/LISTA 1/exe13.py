# Calcular o valor decimal ao dividir o primeiro número pelo segundo
num1 = input()
num2 = int(input())  

# quantidade de casas decimais
div_len = len(str(num2))  # num dígitos do divisor
if div_len == 1:
    # se true vírgula duas casas para a esquerda
    resultado = float(num1) / 100
elif div_len == 2:
    # se true movemos a vírgula uma casa para a esquerda
    resultado = float(num1) / 10
else:
    # se true o número fica inalterado com .0 no final
    resultado = float(num1)
print('%.2f' % resultado)

#resposta errada