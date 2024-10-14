#Você sabe que a compreensão do conceito de proporção é importante e, por isso,
#  toda vez que tem oportunidade você pratica a resolução de problemas associados a esse conceito. 
# Desta vez, você resolveu calcular qual a porcentagem de exercícios que alguém conseguiu resolver 
# de cada uma das quatro listas do nosso curso. Primeiro você lê quantos exercícios há em cada
#  uma das quatro listas e, depois, os numero de exercícios resolvidos em cada lista. 

# quantidade total de exercícios em cd lista
exe_l1 = int(input())
exe_l2 = int(input())
exe_l3 = int(input())
exe_l4 = int(input())

# exercícios resolvidos
exe_resolv_l1 = int(input())
exe_resolv_l2 = int(input())
exe_resolv_l3 = int(input())
exe_resolv_l4 = int(input())

# porcentagem de exercícios resolv
p_l1 = (exe_resolv_l1 / exe_l1) * 100
p_l2 = (exe_resolv_l2 / exe_l2) * 100
p_l3 = (exe_resolv_l3 / exe_l3) * 100
p_l4 = (exe_resolv_l4 / exe_l4) * 100

print('%.1f' % p_l1)
print('%.1f' % p_l2)
print('%.1f' % p_l3)
print('%.1f' % p_l4)