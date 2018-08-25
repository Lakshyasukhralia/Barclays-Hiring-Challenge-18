
def Sub(string):
    l = len(string)
    list = []
    for i in range(l):
        for j in range(i,l):
            list.append(string[i:j+1])
    return list

A = input()
B = input()
S = input()

SX = Sub(S)

count = 0

for i in SX:
    if A in i and B in i:
        count = count + 1

print(count)
