#Problema com Juros Compostos
# Dado o valor inicial e o valor da taxa de juros, 
# seu programa deve calcular qual seriam os valores dos pagamentos quando passados um, dois e três 
# períodos de tempo.

num1 = float(input()) #valor inicial
num2 = float(input()) #tx de juros

juros = num1 * num2
juros_comp1 = juros+num1
juros_comp2 = (juros_comp1 * num2) + juros_comp1
juros_comp3 = (juros_comp2 * num2) + juros_comp2

print('%.2f' % juros_comp1)
print('%.2f' % juros_comp2)
print('%.2f' % juros_comp3)