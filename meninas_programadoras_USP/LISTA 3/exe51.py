# email #1
# Você ficou encarregada de verificar se todas as meninas que se inscreveram para o nosso curso colocaram
# emails válidos em seus registros.
# Dado o número de candidatas inscritas, analise cada email para verificar
# se ele contém o caractere obrigatório de email 
# Seu programa deve informar quantas das entradas não correspondem a um potencial email.

numeros = int(input())

contador = 0

for i in range(numeros):
    email = str(input())
    if "@" not in email:
        contador += 1  # Incrementa o contador se '@' for encontrado
print(contador)
