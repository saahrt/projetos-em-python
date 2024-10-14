#CPF #1 remover caracteres especiais

cpf = input()
numeroscpf = ""

for i in cpf:
    if i.isdigit():
        numeroscpf += i
print(numeroscpf)