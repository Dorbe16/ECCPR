S = input()
G = input()
invers = ""
index = []
cnt = 0
for i in S:
    if i == 'A':
        invers += 'T'
    elif i == 'T':
        invers += 'A'
    elif i == 'C':
        invers += 'G'
    elif i == 'G':
        invers += 'C'
    else:
        break
inversS = "".join(list(reversed(invers)))
inversG = "".join(list(reversed(G)))
for i in range(len(S)):
    if S[i:i+len(G)] == G:
        cnt += 1
        index.append(i)
for i in range(len(inversS)):
    if invers[i:i+len(G)] == inversG:
        cnt += 1
        index.append(i)
print(cnt)
print(*sorted(index))
