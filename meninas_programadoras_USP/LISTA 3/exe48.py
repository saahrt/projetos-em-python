#mostrar os caracteres equivalentes ao numero inserido e o zero equivalendo ao '.'
num1 = int(input())

if num1 == 0:
    print('.')
else:
    for i in range(num1):
        asterisco = '*' * num1
    print(asterisco)