#Voto obrigatório ou facultativo?

idade = int(input())

if idade <= 69 and idade >= 18:
    print("Seu voto é obrigatório")
elif idade >= 16 and idade <= 17 or idade >= 70:
    print("Seu voto é facultativo: você pode votar ou não")
else:
    print("Jovem demais para votar, espere até 16")