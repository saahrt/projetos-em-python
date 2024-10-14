#calcular a divisão inteira e o resto da divisão do primeiro pelo segundo

num1 = int(input()) 
num2 = int(input())

# divisão por zero
if num2 == 0:
    print("Não há divisão por Zero") 
else:
    div_int = num1 // num2
    resto = num1 % num2

    print(div_int)
    print(resto)