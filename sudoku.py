#SUDOKU
matrice = []
bec = 0
coloana = []
for i in range(9):
        linie = input().split()
        matrice.append(linie)
for linie in matrice:
    for i in linie:
        if linie.count(i) > 1:
            print("Gresit")
            bec = 1
            break
if not bec:
    for coloana in list(zip(*matrice)):
        for j in coloana:
            if coloana.count(j) > 1:
                print("Gresit")
                bec = 1
                break
        if bec: break
if not bec: print("Corect")
