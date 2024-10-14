#Balanço #5
# primeira linha: numero do qual queremos calcular a tabuada (valor entre 1 e 99)
# segunda linha: primeiro valor da tabuada a ser gerado (valor entre 1 e 999)
# terceira linha: último valor da tabuada a ser gerado (valor entre 1 e 999)
num1 = int(input())
i = int(input())
i2 = int(input())


print('Tabuada do', num1, 'de', i, 'até', i2)
i2 += 1
for i in range(i, i2):
    resul = num1 * i
    
    print(num1, 'x', i, '=', resul)