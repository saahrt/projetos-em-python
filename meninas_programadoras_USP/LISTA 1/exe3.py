# Seu programa lê quatro valores, um por linha: uma letra, outra letra,
# um caractere especial, outro caractere especial e um inteiro

# Seu programa deve dar três respostas
# - a soma a primeira letra com o primeiro símbolo
# - a soma a segunda letra com o segundo símbolo
# - a soma das duas respostas anteriores multiplicada por pelo inteiro dado

# Notas:
# - a soma de duas sequencias de caracarteres é também chamada de concatenação
# - em inglês, utiliza-se string para sequência de caracteres

# entradas
let1 = input()
let2 = input()
carac1 = input()
carac2 = input()
num = int(input())

result1 = let1 + carac1
result2 = let2 + carac2
resultALL = (result1 + result2) * num

print(result1)
print(result2)
print(resultALL)