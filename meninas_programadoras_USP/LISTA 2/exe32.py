#Read the three coefficients of a quadratic equation and identify the number of real roots of the equation.
#Para determinar o número de raízes reais, usamos o discriminante 
# 𝐷: D = 𝑏^2−4𝑎𝑐
# D>0: A equação tem 2 raízes reais.
# D=0: A equação tem 1 raiz real.
# D<0: A equação tem 0 raízes reais.

num1 = float(input())
num2 = float(input())
num3 = float(input())

D = num2**2 - 4*num1*num3

if D > 0:
    print("2")
elif D == 0:
    print("1")
elif D < 0:
    print("0")