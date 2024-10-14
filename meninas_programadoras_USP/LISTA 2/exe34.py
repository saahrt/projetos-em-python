#imprimir raiz quadrada (exercicio square root)

num1 = float(input())
num2 = float(input())

if num1 < 0:
    print("Raiz quadrada não é um número real.")
else:
    raiz1 = 0
    while raiz1 * raiz1 <= num1:
        raiz1 += 1
    raiz1 -= 1  # Ajusta a raiz porque o último valor passou

    print(raiz1)

    raiz2 = 0
    while raiz2 * raiz2 <= num2:
        raiz2 += 1
    raiz2 -= 1  # Ajusta a raiz porque o último valor passou

    print(raiz2)