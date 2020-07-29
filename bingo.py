#BINGO
n, k = list(map(int, input().split()))
nr = 0
valori = list(map(int, input().split()))
strigate = list(map(int, input().split()))
valori = [i for i in valori if i not in strigate]
if valori != []:
    print(len(valori))
else:
    print("BINGO!")
