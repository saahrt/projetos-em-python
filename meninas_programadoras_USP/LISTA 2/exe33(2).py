#usando if elif

op = input()
num1 = int(input())
num2 = int(input())

if op == "+":
    resultado = num1 + num2
    print(resultado)
elif op == "-":
    resultado = num1 - num2
    print(resultado)
elif op == "*":
    resultado = num1 * num2
    print(resultado)
elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
        print('%.1f' % resultado)
    else:
        print("Erro: Divisão por zero.")
elif op == "//":
    if num2 != 0:
        resultado = num1 // num2
        print(resultado)
    else:
        print("Erro: Divisão por zero.")
elif op == "%":
    if num2 != 0:
        resultado = num1 % num2
        print(resultado)
    else:
        print("Erro: Divisão por zero.")
elif op == "**":
    resultado = num1 ** num2
    print(resultado)
else:
    print("Operador inválido.")
