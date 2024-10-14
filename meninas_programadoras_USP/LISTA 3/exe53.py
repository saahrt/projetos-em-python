# CPF #3
# ENCODING ERROR
# SIZE ERROR

cpf = input()

if not cpf.isdigit():
    print('ENCODING ERROR')
else:
    if len(cpf) == 11:
        print(cpf)
    else:
        print('SIZE ERROR')