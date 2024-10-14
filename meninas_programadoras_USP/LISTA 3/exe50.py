# Histograma C. 0 equivale a uma quebra de linha

seq_num = input()
numeros = ""

for i in seq_num:
    if i.isdigit():  # verificar se o i é um dígito
        numeros += i  # adiciona o número à variável 'numeros'

for j in numeros:  # Itera sobre os números que foram extraídos
    if j == 0:
        print('\n')
    else:
        # Multiplica '*' pelo valor numérico de cada número
        asterisco = '*' * int(j)
        print(asterisco)
