def sortLexo(words):
    words.sort()
    print(words[0])

A = []
string = input()
for i in range(0,len(string)):
    if string[i] not in A:
        A.append(string[i])

B = []
for i in A:
    new_str = string.replace(i,"")
    B.append(new_str)

sortLexo(B)
