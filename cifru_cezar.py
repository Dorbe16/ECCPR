#CIFRU_CEZAR
alfabet = 'abcdefghijklmnopqrstuvwxyzabcdefghij'
ALFABET = alfabet.upper()
s = input()
nouS = ""
index = 0
n = int(input())
chei = []
for i in range(n):
    chei.append(int(input()))
for litera in s:
    if litera not in alfabet and litera not in ALFABET:
        nouS += litera
    elif litera == litera.lower():
        for i in alfabet:
            if i == litera:
                litera = alfabet[alfabet.index(i) + chei[index]]
                nouS += litera
                index += 1
                if index == len(chei):
                    index = 0
                break
    elif litera == litera.upper():
        for i in ALFABET:
            if i == litera:
                litera = ALFABET[ALFABET.index(i) + chei[index]]
                nouS += litera
                index += 1
                if index == len(chei):
                    index = 0
                break
print(nouS)
