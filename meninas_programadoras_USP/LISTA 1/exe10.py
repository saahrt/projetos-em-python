# Dona Maria wants you to answer quickly: given two integer values, what is the result of the mathematical operations 
# addition, subtraction, multiplication, division, modulus, integer division and power between the two? 
# Since you don't have a calculator, you decide to write a program that calculates the answers quickly.
# When necessary, consider values with two decimal places.

num1 = int(input())
num2 = int(input())

soma = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
potencia = num1 ** num2
if num2 != 0:
    div = num1 / num2
    mod = num1 % num2
    div_int = num1 // num2
else:
    div = 'não há divisão por zero'
    mod = 'não há divisão por zero'
    div_int = 'não há divisão por zero'

print(soma)
print(subtraction)
print(multiplication)
print('%.2f'% div)
print(mod)
print(div_int)
print(potencia)