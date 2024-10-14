#Tem o que precisa na senha?
# Dado um caractere qual sua classificacao? 
# - vogal (minúscula ou maiúscula), algarismo, carectere especial ou outro
# Neste caso, um caractere especial é um entre os seguintes: @#$%&*()_-+=!

valor = input()
carac_esp = "@#$%&*()_-+=!"

if valor == 'a' or valor == 'e' or valor == 'i' or valor == 'o' or valor == 'u' or \
       valor == 'A' or valor == 'E' or valor == 'I' or valor == 'O' or valor == 'U':
        print("vogal")

elif valor >= '0' and valor <= '9':
    print("algarismo")

elif valor in carac_esp:
    print("especial")
else:
    print("outro")
