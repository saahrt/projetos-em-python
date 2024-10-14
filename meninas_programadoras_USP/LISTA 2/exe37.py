#mais velha entre 4 irmãs

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if n1 >= n2 and n1 >= n3 and n1 >= n4:
    veia = n1
elif n2 >= n1 and n2 >= n3 and n2 >= n4:
    veia = n2
elif n3 >= n2 and n3 >= n1 and n3 >= n4:
    veia = n3
else:
    veia = n4

print("A mais velha tem", veia, "anos")