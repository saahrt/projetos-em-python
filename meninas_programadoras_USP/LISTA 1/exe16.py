#Given a number of minutes, your program should convert to the corresponding number of hours and minutes.

num1 = int(input())
horas = num1 // 60  
minutos = num1 % 60  

print(f"{num1}min = {horas}h{minutos}min")
