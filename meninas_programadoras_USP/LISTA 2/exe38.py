# Dada a enorme importância do sono, seu programa deve orientar 
# um usuário adulto que informa quantas horas de sono teve na noite anterior.

sono = float(input())

if sono > 8:
    print("Você dormiu muito bem, parabéns!")
elif sono == 8:
    print("Você dormiu o suficiente, continue assim!")
else:
    print("Você precisa de mais tempo de sono, cuide-se!")