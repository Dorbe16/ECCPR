def check(x):
    lista = []
    for i in range(1,len(x)):
        if i == 1:
            lista.append(x[i-1])

        if x[i] != x[i-1]:
            lista.append(x[i])
    return lista
def find(sublist, list):
    for i in range(len(list)):
        if list[i:i + len(sublist)] == sublist:
            return i
maxim = 0
N = int(input())
solduri = list(map(int,input().split()))
variatii = []
siruri = []
sir = []
for i in range(1,len(solduri)):
    delta = solduri[i] - solduri[i-1]
    variatii.append(delta)
for i in range(len(variatii)):
    if variatii[i] >= 0:
        if i < len(variatii) - 1:
            if variatii[i+1] < 0:
                sir.extend([variatii[i], variatii[i+1]])
            else:
                siruri.append(check(sir))
                if len(check(sir)) > maxim:
                    maxim = len(check(sir))
                sir = []
    elif variatii[i] < 0:
        if i < len(variatii) - 1:
            if variatii[i+1] >= 0:
                sir.extend([variatii[i], variatii[i+1]])
            else:
                siruri.append(check(sir))
                if len(check(sir)) > maxim:
                    maxim = len(check(sir))
                sir = []
siruri = [i for i in siruri if len(i) == maxim]
index = find(siruri[-1], variatii)
print(maxim)
if maxim != 0:
    for k in range(index + 1, index + len(siruri[-1]) + 1):
        print(solduri[k], end = " ")
    print()
    print(format(sum(solduri) / len(solduri),'.2f'), format(sum(variatii) / len(variatii), '.2f'))