# Histograma C

seq_num = input()
numeros = ""

for i in seq_num:
    if i.isdigit():  # verificar se o i é um dígito
        numeros += i  # adiciona o número à variável 'numeros'

for j in numeros: # Itera sobre os números que foram extraídos
    asterisco = '*' * int(j) # Multiplica '*' pelo valor numérico de cada número
    print(asterisco)