#CAZINO
n = int(input())
cartea = ""
carti = []
bec = 0
for i in range(n):
    carte = input()
    carti.append(carte)
    if cartea == "":
        for i in carti:
            if carti.count(i) > 2:
                cartea = i
                bec = 1
                break
if not bec:
    print("JOC OK")
else: 
    print(cartea)
