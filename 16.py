n = int(input())
q = int(input())
D = {}

A = [int(i) for i in input().split()]

for j in range(0,q):
    B = [int(j) for j in input().split()]
    D[j] = B

def dec_to_bin(x):
    a = bin(x)[2:]
    if a.count('11')>0:
        return 1
    else:
        return 0

for i,j in D.items():
    c = 0
    for k in range(j[0]-1,j[1]):
        c = c + dec_to_bin(A[k])
    print(c)
