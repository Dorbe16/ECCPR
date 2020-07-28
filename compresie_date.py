#COMPRESIE_DATE
n = int(input())
total = []
for i in range(n):
    linie = list(map(int, input().split(",")))
    linieOut = []
    for j in range(len(linie)):
        if linie[j] != 0:
            if j != len(linie) - 1:
                index = j + 1
            aparitii = 0
            if linie[index] == 0:
                if index <= len(linie):
                    while linie[index] == 0:
                        aparitii += 1
                        if index != len(linie) - 1:
                            index += 1
                        else:
                            break
            if aparitii != 0:
                linieOut.append("(" + str(linie[j]) + "," + str(aparitii) + ")")
            else:
                linieOut.append(linie[j])
    total.append(linieOut)
for k in total:
    print(",".join(list(map(str, k)))) 
