def Sub(string):
    l = len(string)
    list = []
    count = 0

    for i in range(l):
        for j in range(i,l):
            e = string[i:j+1]
            list.append(e)
            if A in e and B in e:
                count = count + l - j 
                break
    return count

A = input()
B = input()
S = input()

print(Sub(S))
