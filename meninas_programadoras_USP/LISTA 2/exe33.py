#match statement para operações (equivalente ao switch case)

op = input()
num1 = float(input())
num2 = float(input())

match op:
    case "+":
        resultado = num1 + num2
        print(resultado)
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(resultado)
        else:
            print("Erro: Divisão por zero.")
    case "//":
        if num2 != 0:
            resultado = num1 // num2
            print(resultado)
        else:
            print("Erro: Divisão por zero.")
    case "%":
        resultado = num1 % num2
        print(resultado)
    case "-":
        resultado = num1 - num2
        print(resultado)
    case "*":
        resultado = num1 * num2
        print(resultado)
    case "**":
        resultado = num1 ** num2
        print(resultado)
    case _:
        print("Operador inválido.")
