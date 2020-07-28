#FORME_GEOMETRICE
n = int(input())
suprafete = []
for i in range(n):
    figura = input().split()
    if figura[0] == 'patrat':
        suprafete.append(tuple([float(figura[1]) ** 2, figura]))
    elif figura[0] == 'dreptunghi':
        suprafete.append(tuple([float(figura[1]) * float(figura[2]), figura]))
    elif figura[0] == 'cerc':
        suprafete.append(tuple([3.14 * (float(figura[1]) ** 2), figura]))
print(*sorted(suprafete, reverse = True)[0][1])
